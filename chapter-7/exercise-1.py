filename = input("Enter a file name: ")
handle = None

try:
  handle = open(f"files/{ filename }", 'r')
except FileNotFoundError:
  print("Failed to open file.")
  quit()

for line in handle:
  print(line.upper().strip())