# From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008

handle = open("files/mbox-short.txt", "r")
times = {}

for line in handle:
  if line.startswith("From"):
    words = line.split()
    if len(words) > 2:
      _time = words[len(words) - 2].split(":")[0]
      times[_time] = times.get(_time, 0) + 1

sorted_keys = list(times)
sorted_keys.sort()

for key in sorted_keys:
  print(key, times[key])