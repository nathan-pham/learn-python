filename = input("Enter a file name: ")
handle = None

try:
  handle = open(f"files/{filename }", 'r')
except FileNotFoundError:
  print("Failed to open file.")
  quit()

prefix = "X-DSPAM-Confidence:"
numbers = []

for line in handle:
  if line.startswith(prefix):
    numbers.append(
      float(line[len(prefix):].strip())
    )

average = sum(numbers) / len(numbers)
print("Average spam confidence:", average)
