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
<!--
github.com/svlentink/resume
-->
<style>
/* basics */
.dataframe thead { display:none; }
.dataframe td:first-child { display:none; }

/* needed for proper print layout */
@page {
  size: A4;
}
body {
  max-width: 210mm;
  min-width: 210mm;
  width: 210mm;
//  height: 297mm;  
  size: A4;
  margin: 0 auto;
  border: initial;
  border-radius: initial;
  min-height: initial;
  box-shadow: initial;
  background: initial;
}
section {
//  page-break-after:always;
  width: 100%;
  margin:0;
  padding:0;
  display:block;
  overflow:hidden;
}

/* additionals */
table {
  border-top: 1px solid;
  padding: 0;
}
td {
  vertical-align: top;
}
ul { margin:0; padding-left: 3mm; }
h1,h2,h3,h4 { margin:1mm; margin-bottom:0; }

/* experience */
#experience {
  max-width: 60%;
  float:left;
}
#experience .dataframe td:nth-child(2) { display:none; }
#experience tr { font-size: 90%; }
#experience tr:nth-child(1) { /* title */
  font-weight: bold;
  font-size: 100%;
}
#experience tr:nth-child(2) { text-align:right; } /* timespan */
#experience table {
  margin-bottom: 0;
}
#experience tr:last-child ul { list-style: none; }
#experience tr:last-child li {
  display: inline-block;
  margin-right: 1mm;
  font-style: italic;
}
#experience tr:last-child li:after { content: ', '; }
#experience tr:last-child li:last-child:after { content: ''; }

/* header (personal) */
#personal .dataframe td:nth-child(2) { display:none; }
h1 {margin-bottom: 2mm; }
#personal:children {
  float: left;
}
#personal p {
  max-width: 60%;
  float: left;
  margin: 0;
  text-align: center;
  font-style: italic;
}
#personal table {
  max-width:35%;
  float:right;
  margin: 0;
  text-align:right;
}
#personal table td { padding: 0; }
#personal h1 {
  width: 100%;
  text-align: center;
}
#personal h3, #personal h4 { display:none; }
#personal tr ul { list-style: none; }
#personal tr:nth-child(1) td { font-weight:bold; } /* name */
#personal tr:nth-child(2) td:after { content: '	\\01F4CD'; } /* location pushpin */
#personal tr:nth-child(3) td:after { content: '	\\0260F'; } /* phone */
#personal tr:nth-child(4) td:after { content: '	\\02709'; } /* envelope */
#personal table { border: 0; }

/* education */
#education table {
  min-width:100%;
  font-size: 80%;
}
#education, #tree {
  max-width: 38%;
  float:right;
}

/* knowledge graph */
#knowledgeoverview { display:none; }

</style>
'''
html += '<section id="personal">\n'   + person2html() + '</section>\n'
html += '<section id="experience">\n' + exps2html()   + '</section>\n'
html += '<section id="education">\n'  + edu2html()    + '</section>\n'
html += '<section id="tree">\n'       + tree2html()   + '</section>\n'
with open('/output/resume-' + lang_pref + '.html','w') as f:
  f.write(html)

