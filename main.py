import os

chapter = int(input("Enter a chapter number: "))
exercise = int(input("Enter an exercise: "))

path = f"chapter-{chapter}/exercise-{exercise}.py"

print("Running", path)
os.system(f"python {path}")