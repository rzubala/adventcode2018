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
  i = 0 - gen
  sum = 0
  for p in list(state):
    sum += i if p == '#' else 0
    i += 1
  return sum  

def calc(filename):
  state, pattern = parse(filename)
  print '\n'.join(pattern)  
  
  for g in range (0,20):  
    state = '...' + state + '...'
    print state
    newState = []
    for i in range(0, len(state) - 5 + 1):
      for p in pattern:
        plant = False
        if isNextPlant(state[i:i+5], p, '#') == '#':
          plant = True
          break
      newState.append('#') if plant else newState.append('.')
    state = ''.join(newState)
  
  print state  
  print sumState(state, 20)    

def main():
  args = sys.argv[1:]

  if not args:
    print 'usage: input.data '
    sys.exit(1)
  
  calc(args[0])
  
if __name__ == '__main__':
  main()
