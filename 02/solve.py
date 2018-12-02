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

def calc(filename):
  two = 0
  three = 0
  with open(filename) as file:
    for line in file:
      txt = line.rstrip('\n')
      stat = countChar(txt)
      two += stat.get("2", 0)
      three += stat.get("3", 0)
  print 'found: ', two, three
  print 'res: ', two * three  

def main():
  args = sys.argv[1:]

  if not args:
    print 'usage: input.data '
    sys.exit(1)
  
  calc(args[0])
  
if __name__ == '__main__':
  main()
