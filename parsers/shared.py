#!/usr/bin/env python

from docx import Document
from docx.shared import Pt
import datetime
import yaml
from os import getenv
from glob import iglob


lang_pref = getenv('COMPILE_LANGUAGE') or 'language_unknown'
lang_dict = {}
for f in iglob('/content/languages/' + lang_pref + '.y*ml'):
  with open(f,'r') as ymlfile:
    lang_dict = yaml.load(ymlfile)

with open('/content/settings.yml', 'r') as f:
  settings = yaml.load(f)


def date2str(inp):
  '''
  Convert 2022-04 to 'April 2022'
  '''
  if isinstance(inp, int):
    return str(inp)
  
  yearstr = inp[:4]
  if len(inp) >= 7:
    monthint = int(inp[5:7])
    monthstr = datetime.date(1900, monthint, 1).strftime('%B')
    return monthstr + ' ' + yearstr
  else:
    return yearstr

def get_max_cols(inp):
  maxcols = 0
  for tpl in inp:
    if len(tpl) > maxcols:
      maxcols = len(tpl)
  return maxcols

# the following function is probably present in pandas
def tuples2monospaced(inp: list, spacing = 1):
  '''
  As input it takes a list of tuples or lists, thus a 2d plane or table
  '''
  inp = [ [str(y) for y in x ] for x in inp ]
  maxcols = get_max_cols(inp)
#
  maxlength_per_col = []
  for i in range(maxcols):
    maxlength_per_col.append(0)
    for tpl in inp:
      if i < len(tpl):
        if len(tpl[i]) > maxlength_per_col[i]:
          maxlength_per_col[i] = len(tpl[i])
#  
  layoutstr = ''
  for i in maxlength_per_col:
    layoutstr += '{:<' + str(i+spacing) + '}'
#  
  result = []
  for tpl in inp:
    line = layoutstr.format(*tpl,'','','','','','','','','') # ugly but it works
    result.append(line)
  return '\n'.join(result)

def tuples2colon(inp: list):
  print('todo')

def tuples2docx(inp: list, doc, colswidths = []):
  '''
  The colswidths should be an array of percentages e.g. [25,50,25]
  '''
  table = doc.add_table(rows=0, cols=get_max_cols(inp))
  lists = []
  for row in inp:
    cells = table.add_row().cells
    for ci in range(len(row)):
      value = row[ci]
      if isinstance(value, list):
        value = '\n'.join(value) #cells[ci].add_paragraph(v, style='List Bullet')
      cells[ci].text = value

  for i in range(len(colswidths)):
    # https://stackoverflow.com/questions/43749177/python-docx-table-column-width
    table.columns[i].width = colswidths[i] * 55000

  doc.add_page_break()
  return doc
