# create module

# mymodule.py
def sayHello():
	print('Hi')

__verion__ = '0.1'


# parent.py
import mymodule
# from mymodule import sayHello,__version__
# from mymodule import *
 # * tidak akan megimport __version__ karena di angap private
mymodule.sayHello()
print('Version '+mymodule.__version__)