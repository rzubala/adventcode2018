#!/usr/bin/python -tt

import sys
import re
import datetime

def fillId(result):
  id = -1
  out = []  
  for r in result:     
    if r[1] > 0:
      id = r[1]
    out.append((r[0], id, r[2], r[3]))
  return out      

def readLines(filename):
  result = []  
  with open(filename) as file:
    for line in file:
      s = re.search(r'\[([^]]+)\] ', line)
      if (s):
        dateStr = s.group(1)
        date = datetime.datetime.strptime(dateStr, '%Y-%m-%d %H:%M')
      id = -1
      s = re.search(r'Guard #(\d+)', line)
      if (s):
        id = int(s.group(1))
      wake = False
      if 'wakes up' in line:
        wake = True  
      sleep = False
      if 'sleep' in line:
        sleep = True 
      result.append((date, id, sleep, wake))
  result.sort(key=lambda r: r[0])
  return fillId(result) 

def getMostSleepId(result):
  sleeps = {}
  last = 0
  for r in result:
    if r[2]:
      last = r[0]
      continue
    elif r[3]:
      cur = r[0]
      diff = (cur - last).total_seconds() / 60.0
      id = r[1]
      cnt = sleeps.get(id, 0)
      sleeps[id] = cnt + diff
    else:
      last = 0
  return sorted(sleeps, key=sleeps.get, reverse=True)[0] 

def getMostMinute(sId, result):
  stat = {}
  last = 0
  for r in result:
    if r[1] != sId:
      continue
    if r[2]:  
      last = r[0]
      continue
    if r[3]:
      cur = r[0]
      for i in range(last.minute, cur.minute):
        cnt = stat.get(i, 0)
        stat[i] = cnt +1 
    elif r[3]:
      last = 0
  minute = sorted(stat, key=stat.get, reverse=True)[0] 
  return (sId, minute)      

def getMostFrequentMinute(result):
  ids = {}
  last = 0
  for r in result:
    if r[2]:
      last = r[0]
      continue
    elif r[3]:
      cur = r[0]
      id = r[1]
      stat = ids.get(id, {})
      for i in range(last.minute, cur.minute):
        cnt = stat.get(i, 0)
        stat[i] = cnt +1 
      ids[id] = stat    
    else:
      last = 0
        
  maxFreq = -1
  maxMinute = -1
  maxId = -1      
  for i in ids:
    stat = ids[i]    
    minute = sorted(stat, key=stat.get, reverse=True)[0]
    if stat[minute] > maxFreq:
      maxMinute = minute
      maxId = i
      maxFreq = stat[minute]
  return (maxId, maxMinute)      

def parse(filename):
  result = readLines(filename)
  sleepId = getMostSleepId(result)
  minute = getMostMinute(sleepId, result)  
  print 'part1:', minute[0], minute[1], minute[0]*minute[1]
  mfreq = getMostFrequentMinute(result)  
  print 'part2:', mfreq[0], mfreq[1], mfreq[0]*mfreq[1]

def main():
  args = sys.argv[1:]

  if not args:
    print 'usage: input.data '
    sys.exit(1)
  
  parse(args[0])
  
if __name__ == '__main__':
  main()
