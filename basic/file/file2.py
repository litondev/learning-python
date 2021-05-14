try:
	with open('file.txt') as f:
		print(f.readlines())
		# print(f.readdd()) -- akan error
except:
	print('Terjadi Kesalahan')
finally:
	print('we does need to close the file')