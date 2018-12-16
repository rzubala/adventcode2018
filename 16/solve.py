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

  lasti = 3  

  res = None  
  if op == 0:
    if a < lasti and b < lasti:
      res = reg[a] + reg[b]
  elif op == 1:
    if a < lasti:
      res = reg[a] + b
  elif op == 2:
    if a < lasti and b < lasti:
      res = reg[a] * reg[b]
  elif op == 3:
    if a < lasti:
      res = reg[a] * b
  elif op == 4:
    if a < lasti and b < lasti:
      res = reg[a] & reg[b]
  elif op == 5:
    if a < lasti:
      res = reg[a] & b
  elif op == 6:
    if a < lasti and b < lasti:
      res = reg[a] | reg[b]
  elif op == 7:
    if a < lasti:
      res = reg[a] | b
  elif op == 8:
    if a < lasti:
      res = reg[a]
  elif op == 9:
    res = a
  elif op == 10:
    if b < lasti:
      res = 1 if a > reg[b] else 0
  elif op == 11:
    if a < lasti:
      res = 1 if reg[a] > b else 0
  elif op == 12:
    if a < lasti and b < lasti:
      res = 1 if reg[a] > reg[b] else 0
  elif op == 13:
    if b < lasti:
      res = 1 if a == reg[b] else 0
  elif op == 11:
    if a < lasti:
      res = 1 if reg[a] == b else 0
  elif op == 12:
    if a < lasti and b < lasti:
      res = 1 if reg[a] == reg[b] else 0
  
  if res:  
    reg[c] = res

def matchOperations(start, stop, o, a, b, c):
  cnt = 0
  for i in range (0,15):
    reg = start[:]
    #print 'before', reg, codes[i], a, b, c
    operation(str(i), a, b, c, reg)
    #print 'after', reg
    if stop == reg:
      cnt += 1
      #print 'operation', codes[i]
  return cnt  

def parse(filename):
  res = []
  before = []
  after = []
  ops = []  
  with open(filename) as file:
    for line in file:
      #print line.rstrip('\n')

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
        #print 'Parse:',before, after, ops
        before = []
        after = []
        ops = []  
  return res
          
def calc(filename):
  res = parse(filename)
  
  cnt = 0  
  for r in res:
    mo = matchOperations(r[0], r[1], r[2][0], r[2][1], r[2][2], r[2][3])  
    if mo >= 3:
      cnt += 1
  print 'cnt', cnt

def main():
  args = sys.argv[1:]

  if not args:
    print 'usage: input.data '
    sys.exit(1)
  
  calc(args[0])
  
if __name__ == '__main__':
  main()
