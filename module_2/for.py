print("List Iteration")
l = ["Geeks", "for", "Geeks"]
for i in l:
    print(i)

print("\nTuple Iteration")
t = ("geeks", "for", "geeks")
for i in t:
    print(i)

print("\nDictionary Iteration")
d = dict()
d['xyz'] = 123
d['abc'] = 345
for i in d:
    print("%s %d" %(i, d[i]))


lis = ["geeks", "for", "geeks"]
for i in range(len(lis)):
    print(lis[i])


list = ["Nikhil", "Da", "Rocha"]
for i in range(len(list)):
    print(list[i])
else:
    print("Inside the block")