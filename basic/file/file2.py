try:
	with open('text.text') as f:
		print(f.readlines())
except:
	print('Terjadi Kesalahan')
finally:
	print('we does need to close the file')