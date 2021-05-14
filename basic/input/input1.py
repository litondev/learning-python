op1 = float(input("Op 1 : "))
op2 = float(input("Op 2 : "))
op = input("Op : ")
convert =  input("Convert : ")

if convert == "string":
	if op == "*":
		result = op1 * op2;
		print(str(int(result)))
	elif op == "/":
		result = op1 / op2;
		print(str(int(result)));
	elif op == "//":
		result = op1 / op2;
		print(str(int(result)));	
	else:
		print("Oprator Not Found")
else:
	print("Convertor Not Found")