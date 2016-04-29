text = "X-DSPAM-Confidence:   0.8475";

spacePos = text.find(" ")
number = text[spacePos::1]
#not really necessary but since we are just learning and playing
strippedNumber = number.lstrip();
result = float(strippedNumber)

print result

