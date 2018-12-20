#!/usr/bin/env python

file_path = "/content/knowledge-tree.yml"

from asciitree import LeftAligned
from collections import OrderedDict as odict
from boltons.iterutils import remap
from shared import *
#import numpy as np
#import pandas as pd

gen_tree_func = LeftAligned()

print('TODO do not show the archive:true elements')

rawdata = {}
with open(file_path, 'r') as ymlfile:
  rawdata = yaml.load(ymlfile)

def get_timeline(inp: dict):
  end = datetime.datetime.now().year
  start = end
  if 'end' in inp:
    if isinstance(inp['end'],dict):
      end = list(inp['end'].keys())[0]
    else:
      end = inp['end']
    inp.pop('end',None)
  if isinstance(inp['start'],dict):
    start = list(inp['start'].keys())[0]
  else:
    start = inp['start']
  inp.pop('start',None)
  return date2str(start), date2str(end)

def to_odict(path, key, value):
  if isinstance(value,dict) and 'start' in value:
    start, end = get_timeline(value)
    newkey = key + ';' + start + ';->;' + end
    return newkey, value #{ 'macaroni':{}}
  if isinstance(value,int):
    return key, { str(value): {}} #str(value)
  elif isinstance(value, str):
    return key, {value: {}}
  elif isinstance(value, dict):
# https://docs.python.org/3.4/library/collections.html?highlight=ordereddict#collections.OrderedDict
    return key, odict(sorted(value.items(), key=lambda t: t[0]))
  return key, value

def asciitree2lists(inp: str, sep = ';'):
  lines = inp.split('\n')
  result = []
  for l in lines:
    arr = l.split(';')
    result.append(arr)
  return result

def saveTree2doc(tree, doc):
  doc.add_heading('Knowledgetree', 2)
  run = doc.add_paragraph().add_run(tree)
  font = run.font
  font.name = 'Courier'
  font.size = Pt(8)
  doc.add_page_break()
  doc.save('/output/tree.docx')

# https://sedimental.org/remap.html
remapped = remap(rawdata, visit=to_odict)
asciitr = gen_tree_func(remapped)
arr = asciitree2lists(asciitr)
finaltree = tuples2monospaced(arr)
saveTree2doc(finaltree,shared_doc)

with open('/output/tree.txt','w') as f:
  f.write(finaltree)

