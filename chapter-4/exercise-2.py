def prompt(message):
  try:
    return float(input(message))
  except ValueError:
    print("Error, please enter numeric input.")
    exit(0)


hours = prompt("Enter hours: ")
rate = prompt("Enter rate: ")

if hours > 40:
  rate *= 1.5

pay = hours * rate
print("Pay:", pay)