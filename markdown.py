"""
 Markdown.py
 0. just print whatever is passed in to stdin
 0. if filename passed in as a command line parameter,
    then print file instead of stdin
 1. wrap input in paragraph tags
 2. convert single asterisk or underscore pairs to em tags
 3. convert double asterisk or underscore pairs to strong tags
"""

import fileinput
import re

inBlock = False

def convertStrong(line):
  line = re.sub(r'\*\*(.*)\*\*', r'<strong>\1</strong>', line)
  line = re.sub(r'__(.*)__', r'<strong>\1</strong>', line)
  return line

def convertEm(line):
  line = re.sub(r'\*(.*)\*', r'<em>\1</em>', line)
  line = re.sub(r'_(.*)_', r'<em>\1</em>', line)
  return line

def convertH1(line):
  line = re.sub(r'\#(.*)', r'<h1>\1</h1>', line)
  line = re.sub(r'_(.*)_', r'<h1>\1</h1>', line)
  return line

def convertH2(line):
  line = re.sub(r'\##(.*)', r'<h2>\1</h2>', line)
  line = re.sub(r'_(.*)_', r'<h2>\1</h2>', line)
  return line

def convertH3(line):
  line = re.sub(r'\###(.*)', r'<h3>\1</h3>', line)
  line = re.sub(r'_(.*)_', r'<h3>\1</h3>', line)
  return line

def convertBlockQuote(line):
  global inBlock
  if inBlock==False:
    if '>' in line:
      line = line.replace('>','<blockquote>')
      inBlock = True
  if inBlock:
    if '>' in line:
      line = re.sub(r'\>(.*)', r'\1</blockquote>', line)
      inBlock = False
  return line

if __name__ == '__main__':
  
  for line in fileinput.input():
    line = line.rstrip()
    line = convertStrong(line)
    line = convertEm(line)
    line = convertH3(line)
    line = convertH2(line)
    line = convertH1(line)
    line = convertBlockQuote(line)
    print '<p>' + line + '</p>',
