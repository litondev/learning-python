try:
	text = input('Input Some : ')
except EOFError:
	print('why you do EOF on me')
except KeyboardInterrupt:
	print('keyboard interrupt')
except ValueError as err:
	print('terjadi Kesalahan')
else:
	print('Oke')