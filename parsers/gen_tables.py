#!/usr/bin/env python

from docx import Document
import datetime

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


# the following function is probably present in pandas
def tuples2monospaced(inp: list, spacing = 1):
  '''
  As input it takes a list of tuples or lists, thus a 2d plane or table
  '''
  maxcols = 0
  for tpl in inp:
    if len(tpl) > maxcols:
      maxcols = len(tpl)
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

tuples2monospaced([('a','bbb','cdef')])

def tuples2colon(inp: list):
  print('todo')

def tuples2docx(inp: list):
  print('todo')

