name = raw_input("Enter file:")
if len(name) < 1 : name = "mbox-short.txt"
handle = open(name)

text = handle.read()
lines=text.split("\n");

tmpStr = "From "
space = " "
tmp = ""
mail = dict();

for string in lines:
	if string.startswith(tmpStr):
		adr = string[5:]
		x = adr.find(space)
		tmp = adr[:x]
		if tmp in mail:
			mail[tmp]=mail[tmp]+1
		else:
			mail[tmp]=1            

#print mail
email = ""
count = 0
for key in mail.keys():
	if mail[key]> count:
		count = mail[key]
		email = key

print email, count