import urllib.request

url = input("Enter a url: ")
handle = urllib.request.urlopen(url)

total_length = 0
for line in handle:
    decoded = line.decode()
    for char in decoded:
        total_length += 1
        if total_length < 3000:
            print(char, end='')

print(total_length)
# Exercise 4: Change the urllinks.py program to extract and count paragraph (p) tags from the retrieved HTML document and display the count of the paragraphs as the output of your program. Do not display the paragraph text, only count them. Test your program on several small web pages as well as some larger web pages.

