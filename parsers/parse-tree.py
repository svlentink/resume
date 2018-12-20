#!/usr/bin/env python

file_path = "/content/knowledge-tree.yml"

import yaml
from asciitree import LeftAligned
from collections import OrderedDict as odict
from boltons.iterutils import remap
import datetime
from gen_tables import *
#import numpy as np
#import pandas as pd

gen_tree_func = LeftAligned()

print('TODO do not show the archive:true elements')
print('Use a mono-spaced font such as Courier!')

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

# https://sedimental.org/remap.html
remapped = remap(rawdata, visit=to_odict)
asciitr = gen_tree_func(remapped)
arr = asciitree2lists(asciitr)
table = tuples2monospaced(arr)
print(table)

