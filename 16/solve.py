#!/usr/bin/python -tt

import sys
import re

codes = ['addr', 'addi', 
         'mulr', 'muli', 
         'banr','bani',
         'borr', 'bori',
         'setr', 'seti',
         'gtir', 'gtri', 'gtrr',
         'eqir', 'eqri', 'eqrr'] 

def opcodes(op):
  return codes.index(op) 

def operation(op, a, b, c, reg):
  if not op.isdigit():
    op = opcodes(op)
  else:
    op = int(op)

  lasti = 4  

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

def matchOperations(start, stop, o, a, b, c):
  cnt = 0
  for i in range (0,16):
    reg = start[:]
    if not operation(str(i), a, b, c, reg):
      continue  
    if stop == reg:
      cnt += 1
  return cnt  

def parse(filename):
  res = []
  before = []
  after = []
  ops = []  
  with open(filename) as file:
    for line in file:
      s = re.search( r'Before: \[(\d+), (\d+), (\d+), (\d+)\]', line)
      if s:
        after = []
        ops = []
        for i in range(1,5):
          before.append(int(s.group(i))) 

      s = re.search( r'(\d+) (\d+) (\d+) (\d+)', line)
      if s:
        for i in range(1,5):
          ops.append(int(s.group(i))) 

      s = re.search( r'After:  \[(\d+), (\d+), (\d+), (\d+)\]', line)
      if s:
        for i in range(1,5):
          after.append(int(s.group(i))) 
        res.append((before, after, ops))
        before = []
        after = []
        ops = []  
  return res
          
def calc(filename):
  res = parse(filename)
  
  cnt = 0  
  for r in res:
    mo = matchOperations(r[0], r[1], r[2][0], r[2][1], r[2][2], r[2][3]) 
    if mo > 2:
      cnt += 1
  print 'cnt', cnt, '/', len(res)

def main():
  args = sys.argv[1:]

  if not args:
    print 'usage: input.data '
    sys.exit(1)
  
  calc(args[0])
  
if __name__ == '__main__':
  main()
