#!/usr/bin/env python

from shared import *

def attribute2tuple(obj,attr):
  value = get_val(obj,attr)
  if value == '':
    return False
  # try to translate the attribute name
  if attr in lang_dict:
    attrname = lang_dict[attr]
  else:
    attrname = attr
  return (attrname,value)

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
  doc.add_heading('Experience', 1)
  for t in tables:
    tuples2docx(t,doc, settings['exp-column-percentage'] or [] )
