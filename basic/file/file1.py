file = open('file.txt','w')
file.write('Hai')
file.close()

file = open('file.text')
while True:
	line = file.readline()

	if len(line) == 0:
		break

	print(line,end=' ')
file.close()