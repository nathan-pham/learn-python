handle = open("files/mbox-short.txt", "r")
emails = {}

for line in handle:
  if line.startswith("From"):
    words = line.split()
    if len(words) > 2:
      email = words[1]
      emails[email] = emails.get(email, 0) + 1

print(emails)