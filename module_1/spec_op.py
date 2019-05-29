a1 = 3
b1 = 3
a2 = "GeeksforGeeks"
b2 = "GeeksforGeeks"
a3 = [1, 2, 3]
b3 = [1, 2, 3]
print(id(a1))
print(id(b1))
print(a1 is not b1)

print(a2 is b2)
print(id(a2))
print(id(b2))

print(a3 is b3)
print(id(a3))
print(id(b3))