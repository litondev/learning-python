try:
	print('Masukan')
	raise ValueError('masukan salah')
except ValueError as err:
	print(err)
finally:
	print('Final')