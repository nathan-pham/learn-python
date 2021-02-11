handle = open("files/mbox-short.txt", "r")
days = {}

for line in handle:
  if line.startswith("From"):
    words = line.split()
    if len(words) > 2:
      day = words[2]
      days[day] = days.get(day, 0) + 1

print(days)