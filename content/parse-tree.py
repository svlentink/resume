#!/usr/bin/env python

import yaml
from asciitree import LeftAligned
from collections import OrderedDict as odict
from boltons.iterutils import remap
from datetime import datetime
#import numpy as np
#import pandas as pd

gen_tree_func = LeftAligned()

tree = {}
with open("/content/knowledge-tree.yml", 'r') as ymlfile:
  tree = yaml.load(ymlfile)

def get_timeline(inp: dict):
  end = datetime.now().year
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
  return str(start), str(end)

def to_odict(path, key, value):
  if isinstance(value,dict) and 'start' in value:
    start, end = get_timeline(value)
    newkey = key + '; ' + start + ' ==> ' + end
    return newkey, value #{ 'macaroni':{}}
  if isinstance(value,int):
    return key, { str(value): {}} #str(value)
  elif isinstance(value, str):
    return key, {value: {}}
  elif isinstance(value, dict):
# https://docs.python.org/3.4/library/collections.html?highlight=ordereddict#collections.OrderedDict
    return key, odict(sorted(value.items(), key=lambda t: t[0]))
  return key, value

# https://sedimental.org/remap.html
remapped = remap(tree, visit=to_odict)
outp = gen_tree_func(remapped)
lines = outp.split('\n')

longestline = 0
for key in range(len(lines)):
  firstpartofline = lines[key].split(';')[0]
  if len(firstpartofline) > longestline:
    longestline = len(firstpartofline)

for key in range(len(lines)):
  line = lines[key]
  if ';' in line:
    arr = line.split(';')
    while len(arr[0]) < longestline:
      arr[0] += ' '
    firstpartofline = line.split(';')[0]
    lines[key] = ''.join(arr)


table = '\n'.join(lines)
print(table)

#cols = [item.split(';') for item in lines]
#print(cols)
#np.matrix(cols)
