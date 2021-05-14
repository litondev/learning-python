my_dic = {
	"name" : "liton",
	"age" : 50
}

print(my_dic["name"])

del my_dic["name"]

print(my_dic)

my_dic["name"] = "litoninot"

print(my_dic)

my_dic.update({
	"no" : "0897667"
})

print(my_dic)

dic1 = {'a' : 1,'b' : 2}
dic2 = {'b' : 3,'c' : 4}

merged = {**dic1,**dic2}

print(merged)