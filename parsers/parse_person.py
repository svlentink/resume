#!/usr/bin/env python

from shared import *

def get_person_data(filepath = "/content/basics.yml"):
  with open(filepath,'r') as ymlfile:
    return yaml.full_load(ymlfile)

def get_person_table(data = get_person_data()):
  table = []
  for i in settings['basics-order']:
    tpl = attribute2tuple(data,i)
    if tpl != False:
      table.append(tpl)
  return table

def person2doc(doc, data = get_person_data()):
  addHead(doc,get_val(data,'doctitle'), 0)
  t = get_person_table(data)
  tuples2docx(t,doc, settings['basics-column-percentage'] or [])

  addHead(doc,'About', 2)
  doc.add_paragraph(get_val(data,'intro'))
  addHead(doc,'Ambition',3)
  doc.add_paragraph(get_val(data,'develop_goal'))

def person2html(data = get_person_data()):
  result = '<h1 id="doctitle">' + get_val(data,'doctitle') + '</h1>'
  result += tuples2html(get_person_table(data))
  result += '<h3>' + get_val(0,'About') + '</h3>'
  result += '<p>' + get_val(data,'intro') + '</p>'
  result += '<h4>' + get_val(0,'Ambition') + '</h4>'
  result += '<p>' + get_val(data,'develop_goal') + '</p>'
  return result

def get_lang_table(data = get_person_data()):
  langtable = get_val(data,'languages')
  table = []
  for i in langtable:
    proficiency = langtable[i]
    pro_str= ("&#9734;" * (5-proficiency)) + ("&#9733;" * proficiency)
    table.append([i,pro_str])
  return table

def lang2doc(data = get_person_data()):
  return None

def lang2html():
  result = '<h2>' + get_val(0, 'Languages') + '</h2>'
  langtable = get_lang_table()
  langhtml = tuples2html(langtable)
  result += langhtml
  return result

