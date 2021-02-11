handle = open("files/mbox-short.txt", "r")
emails = {}

for line in handle:
  if line.startswith("From"):
    words = line.split()
    if len(words) > 2:
      email = words[1]
      emails[email] = emails.get(email, 0) + 1

def maximum(json):
  max_key = None
  max_value = 0
  for key, value in json.items():
    if value > max_value:
      max_key = key
      max_value = value
    
  return f"{max_key} {max_value}"

def minimum(json):
  min_key = None
  min_value = None
  for key, value in json.items():
    if min_value is None:
      min_value = value
      min_key = key
    elif value < min_value:
      min_value = value
      min_key = key

  return f"{min_key} {min_value}"

print(maximum(emails))
print(minimum(emails))