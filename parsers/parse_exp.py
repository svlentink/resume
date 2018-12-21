#!/usr/bin/env python

from shared import *

def load_exps(dir_path = "/content/experience"):
  exps = []
  for f in iglob(dir_path + '/*.y*ml'):
    with open(f,'r') as ymlfile:
      obj = yaml.load(ymlfile)
      if 'end' not in obj:
        obj['end'] = datetime.datetime.now().year
      obj['end'] = str(obj['end']) #make all a str
      if 'archive' not in obj or not obj['archive']:
        exps.append(obj)
      else:
        print('Skipping archived', f)
  
  # sort by end date
  exps.sort(key=lambda obj: obj['end'], reverse=True)
  
  # convert date to long format
  for e in exps:
    if 'end' in e:
      e['end'] = date2str(e['end'])
    if 'start' in e:
      e['start'] = date2str(e['start'])

  return exps

def attribute2tuple(obj,attr):
  if attr not in obj:
    if attr in settings['aggregations']:
      value = []
      for i in settings['aggregations'][attr]:
        indx = str(i)
        tmpval = attribute2tuple(obj, indx)
        if tmpval != False:
          value.append(tmpval[1])
        else:
          value.append(indx) #use it as a string
      value = ''.join(value)
    else:
      return False
  else:
    # we first check if there is a second language added to the original yml file
    if lang_pref in obj and attr in obj[lang_pref]:
      value = obj[lang_pref][attr]
    else:
      value = obj[attr]
    
    value = str(value)
    # now we try to convert the value using our language dictionary
    if value in lang_dict:
      value = lang_dict[value]
  # we do the same for the attribute name, which we also try to translate
  if attr in lang_dict:
    attrname = lang_dict[attr]
  else:
    attrname = attr
  return (attrname,value)

def get_exp_tables(exps = load_exps()):
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
    tuples2docx(t,doc)

