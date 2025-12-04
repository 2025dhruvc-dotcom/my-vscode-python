s = ("a", "b", "c")
print(s)
c = ("v","n")
print(len(c))
print(len(s))

s = ("a",)
print(type(s))
b = ("a")
print(type(b))

tu1 = ("apple", "banana", "cherry")
tu2 = (1, 5, 7, 9, 3)
tu3 = (True, False, False)
tu4 = ()
print(tu1)
print(tu2)
print(tu3)
print(tu4)


tuple1 = ("abc", 34, True, 40, "male")
print(tuple1)


t = tuple([1,2,3])
print(t)


t = tuple(("abc",))
print(t)


x = ("apple", "banana", "cherry")
y = list(x)
y[1] = "kiwi"
x = tuple(y)
print(x)



t = ("a","b","c","d","e")
(*x,y,z) = t
print(x)
(x,*y,z) = t
print(y)
(x,y,*z) = t
print(*z)


