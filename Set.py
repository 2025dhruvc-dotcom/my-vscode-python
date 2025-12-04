myset = {"a", "b"}
print(myset)
set2 = {1,5,7,9,3,3}
print(set2)
set3 = {True, False, False}
print(set3)



set1 = ({"apple","banana","cherry"})
print(type(set1))
print(set1)



set = {"apple","banana", "cherry"}
for x in set:
    print(x)



set = {"apple","banana", "cherry"}
print("banana" in set)



set = {"apple","banana", "cherry"}
set.add("orange")
print(set)
set.add("blackcurrant")
print(set)



set = {"apple","banana", "cherry"}
tropical = {"mango", "pineapple", "papaya"}
set.update(tropical)
print(set)



set = {"apple","banana", "cherry"}
list = ["kiwi","orange"]
set.update(list)
print(set)

a = {"a","b"}
b = {"b","c"}
a.update(b)
print(a)


set = {"apple","banana", "cherry"}
set.remove("banana")
print(set)
set.discard("banana")
print(set)


set = {"1,2"}
set.clear()
print(set)



set1 = {1,2,3}
set2 = {"apple", "banana", "cherry"}
set4 = {"John","elena"}
set3 = set1 | set2 | set4
print(set3)


set1 = {"apple", "banana" ,"cherry"}
set2 = {"union", "banana" ,"inter"}
set3 = set1.intersection(set2)
print(set3)


set1 = {"apple", "banana" ,"cherry"}
set2 = {"google","microsoft","apple"}
set3 = set1.difference(set2)
print(set3)
set3 = set2.difference(set1)
print(set3)



set1 = {"apple", "banana" ,"cherry"}
set2 = {"google","microsoft","apple"}
set3 = set1.symmetric_difference(set2)
print(set3)











