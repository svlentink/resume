#!/usr/bin/env python3

from parse_tree import getTree, tree2doc, tuples2monospaced, tree2html
from parse_exp import exps2doc, get_exp_tables, exps2monospaced, exps2html
from parse_edu import get_edu_table, edu2doc, edu2html
from parse_person import person2doc, person2html
from shared import load_yamls, lang_pref, tuples2html
from docx import Document

# data attributes
tree = getTree()
exptables = get_exp_tables()
expstxt = exps2monospaced(exptables)
expshtml = exps2html(exptables)
edutable = get_edu_table()
edutxt = tuples2monospaced(edutable)
eduhtml = tuples2html(edutable)
edutable2 = get_edu_table(load_yamls('/content/education/other'))
edutxt2 = tuples2monospaced(edutable2)
eduhtml2 = tuples2html(edutable2)

# saving to separate files
with open('/output/education-' + lang_pref + '.txt','w') as f:
  f.write(edutxt)
with open('/output/education-other-' + lang_pref + '.txt','w') as f:
  f.write(edutxt2)
with open('/output/education-' + lang_pref + '.htm','w') as f:
  f.write(eduhtml)
with open('/output/education-other-' + lang_pref + '.htm','w') as f:
  f.write(eduhtml2)
with open('/output/tree.txt','w') as f:
  f.write(tree)
with open('/output/experience-' + lang_pref + '.txt','w') as f:
  f.write(expstxt)
with open('/output/experience-' + lang_pref + '.htm','w') as f:
  f.write(expshtml)


# creating bundled document
doc = Document()
person2doc(doc)
doc.add_page_break()
edu2doc(doc)
doc.add_page_break()
tree2doc(doc, tree)
doc.add_page_break()
exps2doc(doc)
doc.save('/output/resume-' + lang_pref + '.docx')

# creating bundled html
html = '''
<style>
body { max-width: 800px; }
table {
  border: 1px solid;
  padding:3px;
}
td {
  padding: 3px;
  vertical-align: top;
}
#experience table {
  margin-bottom: 30px;
}
.dataframe thead { display:none; }
.dataframe td:first-child { display:none; }
</style>
'''
html += '<section id="personal">'   + person2html() + '</section>'
html += '<section id="education">'  + edu2html()    + '</section>'
html += '<section id="tree">'       + tree2html()   + '</section>'
html += '<section id="experience">' + exps2html()   + '</section>'
with open('/output/resume-' + lang_pref + '.html','w') as f:
  f.write(html)

