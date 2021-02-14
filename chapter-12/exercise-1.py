import re

handle = open("files/mbox-short.txt", "r")

while True:
  arguments = input("> ").split()
  command = arguments.pop(0)
  count = 0

  if command == "exit":
    break
  elif command == "grep":
    pattern = arguments[0]
    for line in handle:
      if re.search(pattern, line):
        count += 1
      
    print(f"mbox-short.txt has {count} lines that matched {pattern}")
  else:
    print("invalid command", command)
