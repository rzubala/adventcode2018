#!/usr/bin/python -tt

import sys

def printR(r, e1, e2):
    cnt = 0
    for j in r:
      if cnt == e1:
        print '('+str(j)+')',
      elif cnt == e2:
        print '['+str(j)+']',
      else:
        print j,
      cnt += 1
    print

def calc(c, x, y):
  r = [x, y]
  e1 = 0
  e2 = 1  
  cn = int(c) 
  prev = 0  
  while True:
    v = list(str(r[e1] + r[e2]))
    v = [int(x) for x in v]
    for j in v:
      r.append(j)
    
    l = len(r)
    e1 = (e1 + r[e1] + 1) % l
    e2 = (e2 + r[e2] + 1) % l
    
    #print r, prev
    #print r[prev:]

    res = ''.join([str(x) for x in r[prev:]]).find(c)
    if res > 0:
      print 'res:', res+prev  
      break
    prev = l - 6
    if prev < 0:
      prev = 0

    if l % 100000 == 0:  
      print 'len: ', l
      
    #part1
    #if l >= cn + 10:
    #  print ''.join([str(x) for x in r[cn:cn+10]])
    #  break

def main():
  args = sys.argv[1:]

  #calc('74501', 3 ,7)
  #calc('9', 3 ,7)
  #calc('51589', 3 ,7)
  calc('074501', 3 ,7)
  #calc('59414', 3 ,7)
  
if __name__ == '__main__':
  main()
