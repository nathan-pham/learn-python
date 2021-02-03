string = "X-DSPAM-Confidence: 0.8475 "
extracted = string[string.find(" ") + 1 : len(string) - 1]
print(float(extracted))