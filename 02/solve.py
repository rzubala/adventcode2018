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

def printCommon(t1, t2):
  i = 0  
  res = []  
  for c in list(t1):
    if c == t2[i]:
      res.append(c)
    i += 1
  print ''.join(res)  

def findClose(lines):
  size = len(lines)
  for i in range(0, size - 1):
    t1 = lines[i]  
    for j in range(i+1, size):
      t2 = lines[j]  
      if t1 != t2:
        if compare(t1, t2):
          printCommon(t1, t2)  
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
