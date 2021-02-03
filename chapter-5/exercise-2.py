# Exercise 2: Write another program that prompts for a list of numbers as above and at the end prints out both the maximum and minimum of the numbers instead of the average.

status_loop = True
all_numbers = []

while status_loop:
  number = input("Enter a number: ")
  if number == "done":
    status_loop = False
  else:
    try:
      all_numbers.append(float(number))
    except ValueError:
      print("Invalid input")

def minimum(a):
  smallest = None
  for number in a:
    if smallest is None or number < smallest:
      smallest = number
  return smallest

def maximum(a):
  largest = 0
  for number in a:
    if number > largest:
      largest = number
  return largest

print("The minimum value is", min(all_numbers))
print("The maximum value is", max(all_numbers))
print("The minimum value is (custom function)", minimum(all_numbers))
print("The maximum value is (custom function)", maximum(all_numbers))