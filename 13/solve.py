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
        carts.append((x,y,tmp,0))
        replaceCart(ty, x, tmp)
      x += 1  
    y += 1
  return carts  

def moveCart(track, cart):
  s = cart[2]
  c = cart[3]
  x = cart[0]  
  y = cart[1]
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
    
  return (x,y,s,c)

def findColision(carts):
  for c in carts:
    tmp = [cart for cart in carts if cart[0] == c[0] and cart[1] == c[1]]
    if len(tmp) > 1:
      return (c[0], c[1])
  return None  


def moveCarts(track, carts):
  while True:
    carts = sorted(carts, key=lambda tup: (tup[1],tup[0]) )
    newCarts = []
    for c in carts:
      newCarts.append(moveCart(track, c))
    carts = newCarts

    printAll(track, carts)
    colision = findColision(carts)
    if colision:
      print 'colision:',colision
      break;  

def printAll(track, carts):
  for c in carts:
    print c
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
