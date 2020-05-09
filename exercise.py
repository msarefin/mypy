# create a dictionary and take input from user and return the meaning of the word

NameList = {
    "Alice"     :"Works at HSBC",
    "James"     :"Works at CBS",
    "Daniel"    :"Works at HBO",
    "Kim"       :"works at CNN",
    "Neils"     :"works at Fox News"

}

name = input("Input a Name: \n")

# print(NameList[name])

if name in NameList:
    print(NameList[name])
else:
    print("Name not Found in list")