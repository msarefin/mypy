# Dictionary is noting but a key value pair
# A dictionary is a collection of unordered, changable and indexed

di = {}
# print(type(di))

d2 = {"Harry":"Burger","Arshad":"Fish","Ankur":"Cheese","Nasir":"cars","Syed":"Watches","Jimmy":"Perfume","Kathlyn":"Jewelry","Jennifer":{"A":"Flowers","B":"Burgers","C":"Cake","D":"Donuts"}}
d2 ["Mohammed"] = "Pizza"
d2 ["Vikas"] = "Fanta"
d2 ["Farhan"] = "Kabab"
print(d2)
d2.pop("Harry")
print(d2["Jennifer"])
print(d2)
print(d2["Mohammed"])

Cars = {
    "Brand" : "Ford",
    "Model" : "Mustang",
    "Year"  :  1946
}
# adding
Cars["Color"] ="Red"
# removing
Cars.pop("Model")
print(Cars)

# find someone in the disctionay
if "Mohammed" in d2:
    print("yes, 'Mohammed' is one of the keys in the disctionary  ")

if "Jimmy" in d2:
    print("yes, 'Jimmy' is part of disctionary ")

# length -- find the number of keys in dictionary
print(len(d2))

# method remove
# remove the last item
d2.popitem();
print(d2)

# delete
# key level

del d2["Jennifer"]
print(d2)

# delete full program

# del d2
# print(d2)

# clear

# d2.clear()
# print(d2)

print(Cars)

# copy

d3 = d2.copy()
print(d3)

mydict = dict(Cars)
print(mydict)

# updating
print(d2.get("Mohammed"))
d2.update({"Mohammed":"Coffee"})
print(d2.get("Mohammed"))

# nested dictionary

User1 = {
    "Name"  :   "Daniel",
    "Age"   :   1966
}
User2 = {
    "Name"  :   "Linus",
    "Year"  :   "2004"
}

print(User1, User2)

User = {
    "User1" :  {
        "Name"  :   "Ankur",
        "Year"  :   "1969"
    },
    "User2" :   {
        "Name"  :   "Luis",
        "Year"  :   "2006"
    }
}

print(User)