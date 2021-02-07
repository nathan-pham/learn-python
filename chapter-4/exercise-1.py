hours = float(input("Enter hours: "))
rate = float(input("Enter rate: "))

if hours > 40:
  rate *= 1.5

pay = hours * rate
print("Pay:", pay)