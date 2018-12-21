#!/usr/bin/env python

from parse_tree import getTree, tree2doc
from parse_exp import exps2doc, get_exp_tables, exps2monospaced
from docx import Document

# data attributes
tree = getTree()
exptables = get_exp_tables()
expstxt = exps2monospaced(exptables)


# saving to separate files
with open('/output/tree.txt','w') as f:
  f.write(tree)
with open('/output/experience.txt','w') as f:
  f.write(expstxt)


# creating bundled document
doc = Document()
tree2doc(doc, tree)
exps2doc(doc, exptables)
doc.save('/output/resume.docx')

