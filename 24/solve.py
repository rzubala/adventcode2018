#!/usr/bin/python -tt

import sys
import re

def parse(filename):
  res = []
  infection = False
  id = 0  
  with open(filename) as file:
    for line in file:
      #print line.rstrip('\n')

      s = re.search(r'Infection', line)
      if s:
        infection = True
        continue

      s = re.search(r'(\d+) units .+ with (\d+) hit points (\((.+)\))? ?with an attack that does (\d+) (.+) damage at initiative (\d+)', line)  
      if s:
        groups = int(s.group(1))
        hit_points = int(s.group(2))
        weak_immune = s.group(4)
        damage = int(s.group(5))
        damage_type = s.group(6)
        initiative = int(s.group(7))

        weaks = []
        immunes = []

        if weak_immune:
          sw = re.search(r'weak to ([^;]+)', weak_immune)
          if sw:
            weaks = sw.group(1).split(',')

          si = re.search(r'immune to ([^;]+)', weak_immune)
          if si:
            immunes = si.group(1).split(',')

        #print infection, groups, hit_points, weaks, immunes, damage, damage_type, initiative
        res.append(Group(id, infection, groups, hit_points, immunes, weaks, initiative, damage, damage_type))
        id += 1
        
        print id, infection, groups, hit_points, immunes, weaks, initiative, damage, damage_type

  return res

def calc(filename):
  res = parse(filename)
  print fight(res)

def fight(groups_initial):
  while True:
    groups = sorted(groups_initial, key=lambda g: (g.getEffectivePower(), g.initiative), reverse=True)
    selected = set()
    for g in groups:
      targets = sorted([en for en in groups if en.infection != g.infection and en.id not in selected and g.getDamage(en)>0], key=lambda x: (g.getDamage(x), x.getEffectivePower(), x.initiative), reverse=True)
      if targets:
        g.target = targets[0]
        selected.add(targets[0].id)
        
    groups = sorted(groups, key=lambda x: x.initiative, reverse=True)
    any_killed = False
    for g in groups:
      if g.target:
        damage = g.getDamage(g.target)
        destroyed = min(g.target.units, damage/g.target.hit_points)
        if destroyed > 0:
          any_killed = True
        g.target.units -= destroyed
        
    groups = [g for g in groups if g.units > 0]
    for g in groups:
      g.target = None

    if not any_killed:
      return 1, imm

    inf = sum([g.units for g in groups if g.infection])
    imm = sum([g.units for g in groups if not g.infection])
    
    if inf == 0:
      return 1, imm
    if imm == 0:
      return 0, inf

def main():
  args = sys.argv[1:]

  if not args:
    print 'usage: input.data '
    sys.exit(1)
  
  calc(args[0])

class Group(object):
  def __init__(self, id, infection, units, hit_points, immunes, weaks, initiative, damage, damage_type):
    self.infection = infection
    self.units = units
    self.hit_points = hit_points
    self.immunes = immunes
    self.weaks = weaks
    self.damage = damage
    self.damage_type = damage_type
    self.target = None
    self.initiative = initiative
    self.id = id

  def getEffectivePower(self):
    return self.units * self.damage

  def getDamage(self, enemy):
    if self.damage_type in enemy.immunes:
      return 0
    elif self.damage_type in enemy.weaks:
      return self.getEffectivePower() * 2
    else:
      return self.getEffectivePower()
  
if __name__ == '__main__':
  main()
