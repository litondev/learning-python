name = input("Say My Name : ")
age = input("Say My Age : ")

if age > 15:
	print("Your Name Is " + name)
	print("Your Age Is " + str(age))
else:
	print("Your Name Is " + name)
	print("Your Age Is " + str(age))

op1 = float(input("Op 1 : "))
op2 = float(input("Op 2 : "))
op = input("Op : ")
convert =  input("Convert : ")

if convert == "string":
	if op == "*":
		result = op1 * op2;
		print(str(result))
	elif op == "/":
		result = op1 / op2;
		print(str(result));
	elif op == "//":
		result = op1 / op2;
		print(str(result));	
	else:
		print("Oprator Not Found")
else:
	print("Convertor Not Found")