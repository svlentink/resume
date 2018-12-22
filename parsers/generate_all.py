#!/usr/bin/env python

from parse_tree import getTree, tree2doc, tuples2monospaced
from parse_exp import exps2doc, get_exp_tables, exps2monospaced
from parse_edu import get_edu_table, edu2doc
from shared import load_yamls
from docx import Document

# data attributes
tree = getTree()
exptables = get_exp_tables()
expstxt = exps2monospaced(exptables)
edutable = get_edu_table()
edustxt = tuples2monospaced(edutable)
edutable2 = get_edu_table(load_yamls('/content/education/other'))
edustxt2 = tuples2monospaced(edutable2)

# saving to separate files
with open('/output/education.txt','w') as f:
  f.write(edustxt)
with open('/output/education-other.txt','w') as f:
  f.write(edustxt2)
with open('/output/tree.txt','w') as f:
  f.write(tree)
with open('/output/experience.txt','w') as f:
  f.write(expstxt)


# creating bundled document
doc = Document()
edu2doc(doc)
tree2doc(doc, tree)
exps2doc(doc, exptables)
doc.save('/output/resume.docx')

