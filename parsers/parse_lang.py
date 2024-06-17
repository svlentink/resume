#!/usr/bin/env python

from shared import *
from parse_person import get_personal_data

def int_to_stars(inp):
  result = ""
  for i in range(inp):
    result += "&#9733;" # black star
  for i in range(5-inp):
    result += "&#9734;" # white star
  return result

def get_lang_table(data = get_person_data()):
  langs = data["languages"]
  table = [(k, int_to_stars(v)) for k, v in langs.items()]
  return table

def edu2doc(doc):
  addHead(doc,'Languages', 1)
  langtable = get_lang_table()
  tuples2docx(edutable,doc, settings['lang-column-percentage'] or [])

def language2html():
  result = '<h2>' + get_val(0, 'Languages') + '</h2>'
  langtable = get_lang_table()
  langhtml = tuples2html(langtable)
  result += langhtml
  return result
