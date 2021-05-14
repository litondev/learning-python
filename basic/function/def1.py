def hey():
	print("Hey")

def hello(name):
	print("Hello " + str(name))

hey()
hello()

def all_person(*person):
	for item in person:
		print(item);

all_person("a","b","c")


def all_person(**person):
	for item in person:
		print(person[item])

all_person({"name":"toni","liton":"hai"})

my_list = [
	{"name" : "Toni","class" : "A"},
	{"name" : "Topik","class" : "B"}
]

def all_person(*person):
	for item_list in person
		print("My Name " + person[item_list].name)
		print("My Class " + person[item_list].class)
		print("================")

all_person(my_list)

# lamda function
points = [ { ‚x‚ : 2, ‚y‚ : 3 }, { ‚x‚ : 4, ‚y‚ : 1 } ] 
points.sort(key=lambda i : i[‚y‚]) 
print(points)