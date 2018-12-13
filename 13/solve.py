#!/usr/bin/python -tt

import sys

def parse(filename):
  res = []
  with open(filename) as file:
    for line in file:
      res.append(list(line.rstrip('\n')))
  return res

def replaceCart(line, ind, cart):
  if cart == '^' or 'v':
    c = '|'
  if cart == '<' or cart == '>':
    c = '-'
  line[ind] = c  

def findCarts(track):
  carts = []  
  y = 0  
  for ty in track:
    x = 0
    for tx in ty:
      tmp = None  
      if tx == '^' or tx == 'v' or tx == '>' or tx == '<':
        tmp = tx
      if tmp:
        carts.append((x,y,tmp,0,0))
        replaceCart(ty, x, tmp)
      x += 1  
    y += 1
  return carts  

def moveCart(track, cart):
  s = cart[2]
  c = cart[3]
  x = cart[0]  
  y = cart[1]
  m = cart[4]  
  if s == 'v':
    y += 1
  elif s == '^':
    y -= 1
  elif s == '<':
    x -= 1
  elif s == '>':
    x += 1
  
  t = track[y][x]
  
  if t == '/' and s == '^':
    s = '>'
  elif t == '/' and s == 'v':
    s = '<'
  elif t == '\\' and s == 'v':
    s = '>'
  elif t == '\\' and s == '^':
    s = '<'
  elif t == '/' and s == '>':
    s = '^'
  elif t == '/' and s == '<':
    s = 'v'
  elif t == '\\' and s == '<':
    s = '^'
  elif t == '\\' and s == '>':
    s = 'v'
  elif t == '+':
    if c%3 == 0: #left
      if s == 'v':
        s = '>'
      elif s == '^':
        s = '<'
      elif s == '<':
        s = 'v'
      elif s == '>':
        s = '^'
    if c%3 == 2: #right
      if s == 'v':
        s = '<'
      elif s == '^':
        s = '>'
      elif s == '<':
        s = '^'
      elif s == '>':
        s = 'v'
    c += 1
    
  return (x,y,s,c, m+1)

def findColision(carts):
  for c in carts:
    tmp = [cart for cart in carts if cart[0] == c[0] and cart[1] == c[1]]
    if len(tmp) > 1:
      return (c[0], c[1])
  return None  

def removeColisions(track, carts):
  res = []
  toremove = []  
  for c in carts:
    tmp = [cart for cart in carts if cart[0] == c[0] and cart[1] == c[1]]
    if len(tmp) > 1:
      for t in tmp:
        toremove.append(t);
  for c in carts:
    if c not in toremove:
      res.append(c)
  return res  

def allmoved(carts, m):
  for c in carts:
    if c[4] != m:
       return False;
  return True     

def moveCarts(track, carts):
  m = 1  
  while True:
    carts = sorted(carts, key=lambda tup: (tup[1],tup[0]) )
    while True:
      i = -1
      for c in carts:
        i += 1
        if c[4] == m:
          continue
        c = moveCart(track, c)
        carts[i] = c
        tmp = len(carts)
        #part2
        carts = removeColisions(track, carts)
        if len(carts) != tmp:
          break
      if allmoved(carts, m):
        break
    m += 1

    #printAll(track, carts)
    
    #part1
    #colision = findColision(carts)
    #if colision:
    #  print 'colision:',colision
    #  break;
    
    #part2
    if len(carts) <= 1:
      print carts[0][0], carts[0][1]
      break

def printCarts(carts):
  for c in carts:
    print c

def printAll(track, carts):
  printCarts(carts)  
  y = 0  
  for ty in track:
    x = 0
    for tx in ty:
      tmp = [cart for cart in carts if cart[0] == x and cart[1] == y]
      if tmp:
        sys.stdout.write(tmp[0][2])
      else:
        sys.stdout.write(tx)
      x += 1
    y += 1
    print    
      
def calc(filename):
  track = parse(filename)
  carts = findCarts(track)
  moveCarts(track, carts)

def main():
  args = sys.argv[1:]

  if not args:
    print 'usage: input.data '
    sys.exit(1)
  
  calc(args[0])
  
if __name__ == '__main__':
  main()
