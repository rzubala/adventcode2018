#!/usr/bin/python -tt

import sys
import re

def isNextPlant(pattern, state, result):
  return result if pattern == state else '.'    

def parse(filename):
  res = [] 
  with open(filename) as file:
    for line in file:
      s = re.search(r'^([^\s]+) => #', line)
      if s:
        res.append(s.group(1))
      else:
        s = re.search(r'initial state: (.+)', line)
        if s:
          state = s.group(1)
          
  return (state, res)     

def sumState(state, gen):
  i = -3
  sum = 0
  for p in list(state):
    sum += i if p == '#' else 0
    i += 1
  return sum  

def ldots(i):
  if i == -2:
    return '....'
  elif i == -1:
    return '...'
  elif i == 0:
    return '..'
  elif i == 1:
    return '.'
  return ''  

def rdots(i):
  if i == 1:
    return '....'
  elif i == 0:
    return '...'
  elif i == -1:
    return '..'
  elif i == -2:
    return '.'
  return ''  

def calc(filename, gen):
  state, pattern = parse(filename)
  state = '...' + state
  g = 0
  last = None  
  while g < gen:
    last = sumState(state, gen)
    newState = []
    l = len(state)
    for i in range(-2, l + 2):
      if i < 2:
        comp = ldots(i) + state[0:i+3]
      elif i > l-3:
        comp = state[i-2:l] + rdots(i-l)  
      else:
        comp = state[i-2:i+3]

      for p in pattern:
        plant = False
        if isNextPlant(comp, p, '#') == '#':
          plant = True
          break
      newState.append('#') if plant else newState.append('.')
    state = ''.join(newState[2:-1])
    g += 1  
  
  sum = sumState(state, gen)    
  print 'sum', g, sumState(state, gen)  
  return (sum, sum - last)

def main():
  args = sys.argv[1:]

  if not args:
    print 'usage: input.data '
    sys.exit(1)
  
  calc(args[0], 20)

  gen = 200  
  sum, diff = calc(args[0], gen)
  gen2 = 50000000000
  print gen2, ':', sum + (gen2 - gen) * diff 
    
if __name__ == '__main__':
  main()
