my_list = [
	{"name" : "Toni","class" : "A"},
	{"name" : "Topik","class" : "B"}
]

def all_person(person):
	for item_list in person:

		for item_child_list in item_list:		
			print(f"My {'class' if item_child_list == 'class' else 'name'} {item_list[item_child_list]}")

		print("================")

all_person(my_list)