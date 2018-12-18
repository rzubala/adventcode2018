#!/usr/bin/python -tt

import sys

def parse(filename):
  res = []
  with open(filename) as file:
    for line in file:
      res.append(list(line.rstrip('\n')))
  return res

def printRes(res):
  for line in res:
    for x in line:
      sys.stdout.write(x)
    print

def getVal(res, y, x):
  if x < 0 or y < 0:
    return None
  if x >= len(res) or y >= len(res):  
    return None
  try:
    return res[y][x]
  except:
    return None

def getNext(prev,res, y, x):
  neighs = []  
  for yn in range(y-1, y+2):
    for xn in range(x-1, x+2):
      if x == xn and y == yn:
        continue
      point = getVal(prev, yn, xn)
      if point:
        neighs.append(point)  

  if res[y][x] == '.' and len([n for n in neighs if n == '|']) > 2:
    res[y][x] = '|'
  elif res[y][x] == '|' and len([n for n in neighs if n == '#']) > 2:
    res[y][x] = '#'
  elif res[y][x] == '#':
    if len([n for n in neighs if n == '#']) > 0 and len([n for n in neighs if n == '|']) > 0:
      res[y][x] = '#'
    else:  
      res[y][x] = '.'


def convert(res, m):

  prev = [row[:] for row in res]  
  y = 0  
  for line in res:
    x = 0
    for c in line:
      cn = getNext(prev,res,y,x)
      x += 1
    y += 1

  print '\nAfter', m   
  printRes(res)  

def calc(filename):
  res = parse(filename)

  printRes(res) 
  for i in range (1, 11):  
    convert(res, i) 

  cntl = 0
  cntt = 0
  for line in res:
    cntt += len([n for n in line if n == '|'])
    cntl += len([n for n in line if n == '#'])

  print 'res', cntl, cntt, cntl * cntt  


def main():
  args = sys.argv[1:]

  if not args:
    print 'usage: input.data '
    sys.exit(1)
  
  calc(args[0])
  
if __name__ == '__main__':
  main()
