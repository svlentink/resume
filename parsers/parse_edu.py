#!/usr/bin/env python

from shared import *

def get_edu_table(edus = load_yamls('/content/education')):
  table = []
  for e in edus:
    row = []
    for i in settings['edu-order']:
      if i in e:
        val = get_val(e,i)
        row.append(val)
      else:
        row.append('')
    table.append(row)
  return table

def edu2doc(doc, edutable = get_edu_table()):
  doc.add_heading('Education', 1)
  tuples2docx(edutable,doc, settings['edu-column-percentage'] or [] )
