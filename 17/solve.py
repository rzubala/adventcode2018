#!/usr/bin/python -tt

import sys
import re

def parse(filename):
  res = {}
  with open(filename) as file:
    for line in file:
      #print line.rstrip('\n')
      s = re.search('y=(\d+), x=(\d+)..(\d+)', line)
      if s:
        y = int(s.group(1))
        xf = int(s.group(2))
        xt = int(s.group(3))
        for x in range(xf,xt+1):
          res[(x,y)] = '#'
      s = re.search('x=(\d+), y=(\d+)..(\d+)', line)
      if s:
        x = int(s.group(1))
        yf = int(s.group(2))
        yt = int(s.group(3))
        for y in range(yf,yt+1):
          res[(x,y)] = '#'

  return res

def printRes(res):
  minx = min(res, key = lambda t: t[0])[0]  
  maxx = max(res, key = lambda t: t[0])[0]  
  miny = min(res, key = lambda t: t[1])[1]  
  maxy = max(res, key = lambda t: t[1])[1] 

  for y in range (0, maxy+2):
    for x in range (minx-1, maxx+2):
      if x == 500 and y == 0:
        sys.stdout.write('+')
        continue
      val = res.get((x,y))
      if val: 
        sys.stdout.write(val)
      else:
        sys.stdout.write('.')
    print
  print      

def goSide(res, p, left, cnt):
  if left:  
    p = (p[0] - 1, p[1])
    minx = min(res, key = lambda t: t[0])[0]  
    if p[0] < minx:
      return None
  else:  
    p = (p[0] + 1, p[1])
    maxx = max(res, key = lambda t: t[0])[0]  
    if p[0] > maxx:
      return None
    
  resd = goDown(res, p, cnt + 1)
  if not resd:  
    res[p] = '|'
    return None  

  val = res.get(p)
  if val == '~' or val == '#':
    return p[0]

  res[p] = '|'
  return goSide(res, p, left, cnt + 1)

def goDown(res, p, cnt):
  p = (p[0], p[1] + 1)

  maxy = max(res, key = lambda t: t[1])[1]
  if p[1] > maxy:
    return False

  val = res.get(p)
  if val == '~' or val == '#':
    return True

  if goDown(res, p, cnt + 1):
    resl = goSide(res, p, True, cnt + 1)
    resr = goSide(res, p, False, cnt + 1)
    if resl and resr:
      for x in range(resl+1, resr):
        res[(x,p[1])] = '~'
      return True

  res[p] = '|'
  return False

def flow(res):
  p = (500, 0)
  cnt = 0  
  goDown(res, p, cnt)

  print len([x for x in res if res[x] == '~' or res[x] == '|'])  

def calc(filename):
  res = parse(filename)
  #printRes(res)
  flow(res)  
  printRes(res)

def main():

  sys.setrecursionlimit(10000)

  args = sys.argv[1:]

  if not args:
    print 'usage: input.data '
    sys.exit(1)
  
  calc(args[0])
  
if __name__ == '__main__':
  main()
