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

def sum(a):
  _sum = 0
  for number in a:
    _sum += number
  return _sum

all_sum = sum(all_numbers)

print("The total is", all_sum)
print("The count is", len(all_numbers))
print("The average is", all_sum / len(all_numbers))