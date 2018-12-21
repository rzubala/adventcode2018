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

  res = None  
  if op == 0:
    res = reg[a] + reg[b]
  elif op == 1:
    res = reg[a] + b
  elif op == 2:
    res = reg[a] * reg[b]
  elif op == 3:
    res = reg[a] * b
  elif op == 4:
    res = reg[a] & reg[b]
  elif op == 5:
    res = reg[a] & b
  elif op == 6:
    res = reg[a] | reg[b]
  elif op == 7:
    res = reg[a] | b
  elif op == 8:
    res = reg[a]
  elif op == 9:
    res = a
  elif op == 10:
    res = 1 if a > reg[b] else 0
  elif op == 11:
    res = 1 if reg[a] > b else 0
  elif op == 12:
    res = 1 if reg[a] > reg[b] else 0
  elif op == 13:
    res = 1 if a == reg[b] else 0
  elif op == 14:
    res = 1 if reg[a] == b else 0
  elif op == 15:
    res = 1 if reg[a] == reg[b] else 0
  else:
      return None

  reg[c] = res
  return True 

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
  reg0 = None
  reg0l = []

  ipc = reg[ip]
  ilen = len(ins)
  while ipc < ilen:

    if ipc == 28:
      reg4 = reg[4]
      #part 1
      #print 'lowest value', reg4
      if reg4 in reg0l:
        # part 2
        print 'highest value', reg0
        return

      reg0 = reg4
      reg0l.append(reg4)

    r = ins[ipc]
    operation(r[0], r[1], r[2], r[3], reg)
    ipc = reg[ip] + 1
    reg[ip] = ipc
    #print reg

def main():
  args = sys.argv[1:]

  if not args:
    print 'usage: input.data '
    sys.exit(1)
  
  calc(args[0])
  
if __name__ == '__main__':
  main()
