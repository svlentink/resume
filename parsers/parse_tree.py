#!/usr/bin/env python

from asciitree import LeftAligned
from collections import OrderedDict as odict
from boltons.iterutils import remap
from shared import *
from glob import glob
#import numpy as np
#import pandas as pd

gen_tree_func = LeftAligned()

print('TODO do not show the archive:true elements')

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

def getTree(file_path = "/content/knowledge-tree.yml"):
  rawdata = {}
  with open(file_path, 'r') as ymlfile:
    rawdata = yaml.full_load(ymlfile)
  # https://sedimental.org/remap.html
  remapped = remap(rawdata, visit=to_odict)
  asciitr = gen_tree_func(remapped)
  arr = asciitree2lists(asciitr)
  finaltree = tuples2monospaced(arr)
  return finaltree

def getTreeAsSet(key, value, result=set()):
  if isinstance(value,dict) and ('start' in value or not value): #also empty dicts
    result.add(key)
  elif isinstance(value, str):
    result.add(key)
  elif isinstance(value, dict):
    for k, v in value.items():
      getTreeAsSet(k, v, result)

def getOtherstr(file_path = "/content/other-knowledge.txt"):
  data = []
  with open(file_path, 'r') as f:
    data = f.read().split('\n')
  data.sort()
  removed_empty = filter(len, data)
  return removed_empty

def getAllTech():
  file_path = "/content/knowledge-tree.yml"
  rawdata = {}
  with open(file_path, 'r') as ymlfile:
    rawdata = yaml.full_load(ymlfile)
  treeset = set()
  getTreeAsSet('',rawdata,treeset)

  otherset = set(getOtherstr())

  files_path = "/content/experience/*.yml"
  expset = set()
  for f in glob(files_path):
    with open(f, 'r') as ymlfile:
      rawdata = yaml.full_load(ymlfile)
      if 'tech' in rawdata:
        for key in rawdata['tech']:
          expset.add(key)

  return treeset.union(otherset).union(expset)

def getAllTechStr():
  l = list(getAllTech())
  s = sorted(l, key = lambda x: str(x).casefold())
  return ', '.join(s)

def tree2doc(doc, tree = getTree(), other=getOtherstr()):
  addHead(doc,'Knowledge fields', 1)
  run = doc.add_paragraph().add_run(tree)
  font = run.font
  font.name = 'Courier'
  font.size = Pt(8)
  addHead(doc,'Other',2)
  doc.add_paragraph(', '.join(other))

def tree2html(tree = getTree(), other=getOtherstr()):
  result = '<div id="knowledgeoverview">'
  result +='<h2>' + get_val(0, 'Knowledge fields') + '</h2>'
  result += '<pre><code style="font-family:monospace;">\n'
  result += tree + '\n</code></pre>'
  result += '<h3>' + get_val(0, 'Other') + '</h3>'
  result += '<span>' + ', '.join(other) + '</span>'
  result += '</div>\n'
  result += '<h2>' + get_val(0, 'Techniques') + '</h3>'
  result += '<span>' + getAllTechStr() + '</span>'
  return result

