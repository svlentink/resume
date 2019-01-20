#!/usr/bin/env python

from shared import *

def get_exp_tables(exps = load_yamls("/content/experience")):
  tables = []
  for e in exps:
    rows = []
    for i in settings['exp-order']:
      tpl = attribute2tuple(e,i)
      if tpl != False:
        rows.append(tpl)
    tables.append(rows)
  return tables

def exps2monospaced(tables = get_exp_tables()):
  blob = ''
  for t in tables:
    blob += tuples2monospaced(t) + '\n\n'
  return blob

def exps2doc(doc, tables = get_exp_tables()):
  addHead(doc,'Experience', 1)
  for t in tables:
    tuples2docx(t,doc, settings['exp-column-percentage'] or [])
    doc.add_paragraph(' \n \n ')

def exps2html(tables = get_exp_tables()):
  if len(tables):
    y = tables.pop()
    x = exps2html(tables)
    return x + tuples2html(y)
  else:
    return '<h2>' + get_val(0,'Experience') + '</h2>'
    
