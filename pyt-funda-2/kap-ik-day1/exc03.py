import os
os.system('cls')
# Part 3 · Strings in Depth
print('#'*20)
route_name = "12A Express"
print(route_name[0])
print(route_name[-11])

print(route_name[10])
print(route_name[-1])

print(route_name[0:3])
print(route_name[3:6])
print(route_name[6:])

print(route_name[::-1])
print('#'*20)
print(f'{route_name[0::]:<20}')
print('#'*20)
print(f'{route_name[0::]:>20}')
print('#'*20)
print(f'{route_name[0::]:^20}')
print('#'*20)
print(route_name[0::2])

print(route_name[-1::-1])

print(f'What is here: {route_name[4:-2:-1]}')
print('#'*20)
'''
  Method            What it does                      Example
  ────────────────  ────────────────────────────────  ─────────────────────────────
  .upper()          ALL CAPS                          "12a express".upper() → "12A EXPRESS"
  .lower()          all lowercase                     "12A EXPRESS".lower() → "12a express"
  .strip()          remove leading/trailing spaces    " Central ".strip()  → "Central"
  .split(sep)       split into a list                 "A,B,C".split(",")   → ['A','B','C']
  .join(list)       join list into string             ",".join(['A','B'])   → "A,B"
  .replace(a,b)     replace all occurrences           "bus stop".replace("stop","stand")
  .find(sub)        index of first match (-1 if none) "Express".find("press") → 2
  .startswith(s)    does it start with s?             "12A".startswith("12") → True
  .endswith(s)      does it end with s?               "Express".endswith("ss") → True
  .count(sub)       how many times does sub appear?   "abcabc".count("bc")   → 2
  '''