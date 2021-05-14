my_list = []
my_list1 = [1,2,3,4,5]
my_list2 = ["a","b","c","d","e"]

print(my_list1 + [6,7])

my_list1.append(10)

print(my_list1)

my_list1.pop()

print(my_list1)

print(len(my_list2));

# list 2 dimension
my_list3 = [
	["a","b","c"],
	["aa","bb","cc"]
]

print(my_list3)

# list with dic
my_list4 = [
	{"name" : "Toni","class" : "A"},
	{"name" : "Liton","class" : "B"}
]

print(my_list4)

# menemukan data yang sering digunakan
test = [1,2,3,3,4];
print(max(set(test),key = test.count))

mylist = [i for i in range(10)]
print(mylist)

mylist = [x**2 for x in range(10)]
print(mylist)

def some_function(a):
	return (a + 5) / 2
my_formula = [some_function(i) for i in range(10)]
print(my_formula)

mylist = [i for i in range(10) if i%2 == 0]
print(mylist)

revarray = [1,2,3,4,5][::-1]
print(revarray)

def upper_s(s):
	return s.upper()
mylist = list(map(upper_s,['s','a']))
print(mylist)

list_of_ints = list(map(int,"12345"))
print(list_of_ints)

print(set([1,2,3,3,4,5,6]))
