
table = {
  "A": 0.9,
  "B": 0.8,
  "C": 0.7,
  "D": 0.6
}


try:
  score = float(input("Enter a score: "))

  if score < 0.6:
    print("F")
  else:
    for grade in table:
      if score >= table[grade]:
        print(grade)
        break
except ValueError:
  print("Bad score")