for item in range(0,5):
	print(item)
else:
	print('else')

# multi list looping
my_list1 = [
	["a","b","c"]
]

for item in my_list1:
	print(item)
	for item_child in item:
		print(item_child)
else:
	print('else')