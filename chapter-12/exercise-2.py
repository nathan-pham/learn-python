import re
import math

handle = open("files/mbox-short.txt", "r")
numbers = []

for line in handle:
  trimmed = line.strip()
  match = re.findall("New Revision: ([0-9]+)", trimmed)
  if len(match) > 0:
    numbers.append(int(match[0]))

print(math.floor(sum(numbers) / len(numbers)))