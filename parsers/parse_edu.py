#!/usr/bin/env python

from shared import *

def get_edu_table(edus = load_yamls('/content/education'), order=settings['edu-order']):
  table = []
  for e in edus:
    row = []
    for i in order:
      if i == 'fromto':
        st = get_val(e,'start')
        en = get_val(e,'end')
        if st == en:
          val = st
        elif st == '':
          val = en # certificates only have end date
        else:
          val = get_val(e,i)
      else:
        val = get_val(e,i)
      row.append(val)
    table.append(row)
  return table

def edu2doc(doc):
  addHead(doc,'Education', 1)
  edutable = get_edu_table()
  tuples2docx(edutable,doc, settings['edu-column-percentage'] or [], pagebreak=False)
  addHead(doc,'Certificates and courses',2)
  edutable2 = get_edu_table(load_yamls('/content/education/other'),settings['eduoth-order'])
  tuples2docx(edutable2,doc, settings['eduoth-column-percentage'] or [] )

