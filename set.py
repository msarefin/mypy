s = set()
print(type(set))

s_from_list = set([1,2,3,4,5])

print(s_from_list)
print(type(s_from_list))

s.add(1)
print(s)
print(type(s))

s.add(2)
s.add(3)
s.add(4)
s.add(5)
s.add(6)
print(s,type(s))

s1 = s.union({9,8,7,3})
print(s, s1)

# s.remove("3")
print(s)

s.remove(3)
print(s)

# Removing element
thisset = {"1","2","3","5"}
thisset.remove("2")
thisset.discard("5")
print(thisset)


set1 = {"1","2","3"}
set2 ={"1","2","3","4"}
set = set1.union(set2)
print(set)

alp = {"a","b","c"}
set1.update(alp)
print(set1)
print("This is union")
set.union(alp);
print(set)