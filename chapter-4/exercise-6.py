def prompt(message):
  try:
    return float(input(message))
  except ValueError:
    print("Error, please enter numeric input.")
    exit(0)


def compute_pay(hours, rate):
  if hours > 40:
    rate *= 1.5

  return hours * rate

hours = prompt("Enter hours: ")
rate = prompt("Enter rate: ")

print(compute_pay(hours, rate))