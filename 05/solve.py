#!/usr/bin/python -tt

import sys
from string import ascii_lowercase


def reduce(a):
  ar = a[:]  
  i = 0  
  while True:
    if i+1 >= len(ar):
      break  
    if ar[i].lower() == ar[i+1].lower() and ar[i] != ar[i+1]:
      del ar[i]
      del ar[i]
      if i>0:
        i -= 1
      continue  
    i += 1
  return len(ar)

def parse(a):
  print 'length:', reduce(list(a)) 
  min = len(a)  
  for c in ascii_lowercase:
    tmp = a.replace(c, '')
    tmp = tmp.replace(c.upper(), '')
    cur = reduce(list(tmp))
    if cur < min:
      min = cur
  print min  

def calc(filename):
  with open(filename) as file:
    for line in file:
      ar = line.strip()
      parse(ar)
      return

def main():
  args = sys.argv[1:]

  if not args:
    print 'usage: input.data '
    sys.exit(1)
  
  calc(args[0])
  
if __name__ == '__main__':
  main()
