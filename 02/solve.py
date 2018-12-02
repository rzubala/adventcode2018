#!/usr/bin/python -tt

import sys

def countChar(txt):
  txta = list(txt)
  stat = {}  
  for c in txta:
    cnt = stat.get(c, 0) + 1
    stat[c] = cnt

  two = 0
  three = 0
  for k in stat:
    cnt = stat.get(k)
    if cnt == 2:
      two = 1
    if cnt == 3:
      three = 1
  res = {"2" : two,"3" : three}
  return res

def compare(txt1, txt2):
  a1 = list(txt1)
  a2 = list(txt2)
  cnt = 0
  for i in range(len(a1)):
    if a1[i] != a2[i]:
      cnt += 1;
    if cnt > 2:
      return False
  return cnt == 1

def findClose(lines):
  for t1 in lines:
    for t2 in lines:
      if t1 != t2:
        if compare(t1, t2):
          print t1
          print t2
          return

def calc(filename):
  two = 0
  three = 0
  lines = []  
  with open(filename) as file:
    for line in file:
      txt = line.rstrip('\n')
      lines.append(txt)
      stat = countChar(txt)
      two += stat.get("2", 0)
      three += stat.get("3", 0)
  print 'found: ', two, three
  print 'res: ', two * three  

  findClose(lines)

def main():
  args = sys.argv[1:]

  if not args:
    print 'usage: input.data '
    sys.exit(1)
  
  calc(args[0])
  
if __name__ == '__main__':
  main()
