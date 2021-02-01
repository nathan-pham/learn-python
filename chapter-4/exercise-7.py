table = {
  "A": 0.9,
  "B": 0.8,
  "C": 0.7,
  "D": 0.6
}

def compute_grade(score):
  if score < 0.6:
    return "F"
  else:
    for grade in table:
      if score >= table[grade]:
        return grade
        break

try:
  score = float(input("Enter a score: "))
  print(compute_grade(score))
except ValueError:
  print("Bad score")