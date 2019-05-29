class Test:

    def __init__(self, limit):
        self.limit = limit

    def __iter__(self):
        self.x = 10
        return self

    def __next__(self):
        x = self.x
        if x > self.limit:
            raise StopIteration

        self.x = x + 1
        return x
    

for i in Test(15):
    print(i)

for i in Test(5):
    print(i)



print("Inbuilt Iteration")

print("\nList Iteration")
l = ["geeks", "for", "geeks"]
for i in l:
    print(i)

print("\nTuple Iteration")
t = ("geeks", "for", "geeks")
for i in t:
    print(i)

print("\nString Iteration")
s = "Geeks"
for i in s:
    print(i)

print("\nDictionary Iteration")
d = dict()
d['xyz'] = 123
d['abc'] = 345

for i in d:
    print("%s %d" %(i, d[i]))