#!/usr/bin/python -tt

import sys

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
      print 'operation', codes[i]
  return cnt  

def parse(filename):
  res = []
  with open(filename) as file:
    for line in file:
      print line.rstrip('\n')
  return res

def calc(filename):
  res = parse(filename)

  print matchOperations([3, 2, 1, 1], [3, 2, 2, 1], 9, 2, 1, 2)  
  

def main():
  args = sys.argv[1:]

  if not args:
    print 'usage: input.data '
    sys.exit(1)
  
  calc(args[0])
  
if __name__ == '__main__':
  main()
