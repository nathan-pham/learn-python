"""
Exercise 3: Write a program that reads a file and prints the letters in decreasing order of frequency. Your program should convert all the input to lower case and only count the letters a-z. Your program should not count spaces, digits, punctuation, or anything other than the letters a-z. Find text samples from several different languages and see how letter frequency varies between languages. Compare your results with the tables at https://wikipedia.org/wiki/Letter_frequencies.

"""

alphabet = "abcdefghijklmnopqrstuvwxyz"
count = {}

handle = open("files/romeo.txt")

for line in handle:
  for letter in line.strip():
    if letter in alphabet:
      count[letter] = count.get(letter, 0) + 1

temp = []
for key, value in count.items():
  temp.append(
    (int(value), key)
  )

temp.sort()

for key, value in temp:
  print(value, key)