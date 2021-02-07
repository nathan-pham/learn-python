handle = open("files/romeo.txt")
all_words = []

for line in handle:
  words = line.split()
  for word in words:
    if not word in all_words:
      all_words.append(word)

all_words.sort()

print(all_words)