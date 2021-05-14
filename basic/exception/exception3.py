try:
	print('Masukan Data')
	raise ValueError('Masukan Data Anda Salah')
	print('Lolos')
except ValueError as err:
	print(err)