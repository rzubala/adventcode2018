#!/usr/bin/python -tt

import sys
import re

def parse(filename):
  res = []
  with open(filename) as file:
    for line in file:
      #print line.rstrip('\n')
      s = re.search(r'pos=<(.+),(.+),(.+)>, r=(\d+)', line)
      if s:
        x = int(s.group(1))
        y = int(s.group(2))  
        z = int(s.group(3))  
        r = int(s.group(4))
        res.append((x,y,z,r))
      else:  
        print 'error'
        sys.exit(1)
  return res

def distance(n, nx):
  return abs(nx[0] - n[0]) + abs(nx[1] - n[1]) + abs(nx[2] - n[2])

def inRange(n, nx, self, delta):
  d = distance(n,nx)
  r = nx[3] if self else n[3]  
  return True if (d - r)/delta <= 0 else False

def nanoresCnt(t, res, self, delta):    
  cnt = 0  
  for n in res:
    cnt += 1 if inRange(n, t, self, delta) else 0
  return cnt

def findLocation(res):
  delta = 1
  
  minx = min(res, key = lambda t: t[0])[0]   
  maxx = max(res, key = lambda t: t[0])[0]   
  miny = min(res, key = lambda t: t[1])[1]   
  maxy = max(res, key = lambda t: t[1])[1]   
  minz = min(res, key = lambda t: t[2])[2]   
  maxz = max(res, key = lambda t: t[2])[2]   

  widthx = maxx - minx

  while True:
    if delta > widthx:
      break
    delta = delta * 2  

  while True:
    foundNano = 0
    loc = None

    for z in range(minz, maxz + 1, delta):
      for y in range(miny, maxy + 1, delta):
        for x in range(minx, maxx + 1, delta):
          cnt = nanoresCnt((x,y,z), res, False, delta)    
          if cnt > 0 and cnt == foundNano and isCloser((x,y,z), loc) or cnt > foundNano:
            foundNano = cnt
            loc = (x,y,z)

    if delta == 1:
      return distance(loc, (0,0,0))
    else:
      minx = loc[0] - delta   
      maxx = loc[0] + delta   
      miny = loc[1] - delta   
      maxy = loc[1] + delta   
      minz = loc[2] - delta   
      maxz = loc[2] + delta   
      delta = delta/2
            
def isCloser(p1, p2):
  d1 = distance(p1, (0,0,0))  
  d2 = distance(p2, (0,0,0))  
  return d1 < d2    

def calc(filename):
  res = parse(filename)
  maxn = max(res, key = lambda t: t[3])

  print nanoresCnt(maxn, res, True, 1)    

  print findLocation(res)  
  print findLocation1(res)  

def main():
  args = sys.argv[1:]

  if not args:
    print 'usage: input.data '
    sys.exit(1)
  
  calc(args[0])
  
if __name__ == '__main__':
  main()
