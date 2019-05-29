#list = ["Geeks", "for", "Geeks"]
str="GeeksforGeeks"
for l in str:
    if l == 'e' or l == 's':
        continue
    print("Current letter ", l)


str="Nikhilgeeks"

for l in str:
    if l == 'e' or l == 's':
        break
    print("Current letter ", l)


for l in 'geeksforgeeks':
    pass
print("last letter ", l)