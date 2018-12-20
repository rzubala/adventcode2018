#!/usr/bin/python -tt

import sys
import re

def getOpNum(opc):
  codes = ['addr', 'addi', 
         'mulr', 'muli', 
         'banr','bani',
         'borr', 'bori',
         'setr', 'seti',
         'gtir', 'gtri', 'gtrr',
         'eqir', 'eqri', 'eqrr']
  return codes.index(opc)

def operation(opc, a, b, c, reg):
  op = getOpNum(opc)

  lasti = 6 

  res = None  
  if op == 0:
    if a < lasti and b < lasti:
      res = reg[a] + reg[b]
    else:
      return None  
  elif op == 1:
    if a < lasti:
      res = reg[a] + b
    else:
      return None  
  elif op == 2:
    if a < lasti and b < lasti:
      res = reg[a] * reg[b]
    else:
      return None  
  elif op == 3:
    if a < lasti:
      res = reg[a] * b
    else:
      return None  
  elif op == 4:
    if a < lasti and b < lasti:
      res = reg[a] & reg[b]
    else:
      return None  
  elif op == 5:
    if a < lasti:
      res = reg[a] & b
    else:
      return None  
  elif op == 6:
    if a < lasti and b < lasti:
      res = reg[a] | reg[b]
    else:
      return None  
  elif op == 7:
    if a < lasti:
      res = reg[a] | b
    else:
      return None  
  elif op == 8:
    if a < lasti:
      res = reg[a]
    else:
      return None  
  elif op == 9:
    res = a
  elif op == 10:
    if b < lasti:
      res = 1 if a > reg[b] else 0
    else:
      return None  
  elif op == 11:
    if a < lasti:
      res = 1 if reg[a] > b else 0
    else:
      return None  
  elif op == 12:
    if a < lasti and b < lasti:
      res = 1 if reg[a] > reg[b] else 0
    else:
      return None  
  elif op == 13:
    if b < lasti:
      res = 1 if a == reg[b] else 0
    else:
      return None  
  elif op == 14:
    if a < lasti:
      res = 1 if reg[a] == b else 0
    else:
      return None  
  elif op == 15:
    if a < lasti and b < lasti:
      res = 1 if reg[a] == reg[b] else 0
    else:
      return None  
  else:
      return None

  if c < lasti:  
    reg[c] = res
    return True
  return None  

def parse(filename):
  res = []
  ip = None  
  with open(filename) as file:
    for line in file:
      s = re.search(r'(\w+) (\d+) (\d+) (\d+)', line)
      if s:
        op = s.group(1)
        a = int(s.group(2))
        b = int(s.group(3))
        c = int(s.group(4))
        res.append((op, a, b, c))
        continue
      s = re.search(r'#ip (\d+)', line)
      if s:
        ip = int(s.group(1))

  return ip, res

def calc(filename):
  ip, ins = parse(filename)
  reg = [0, 0, 0, 0, 0, 0]

  ipc = reg[ip]
  ilen = len(ins)
  while ipc < ilen:
    r = ins[ipc]
    operation(r[0], r[1], r[2], r[3], reg)
    ipc = reg[ip] + 1
    reg[ip] = ipc
  print 'value', reg[0]

def main():
  args = sys.argv[1:]

  if not args:
    print 'usage: input.data '
    sys.exit(1)
  
  calc(args[0])
  
if __name__ == '__main__':
  main()
