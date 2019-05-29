print("C style way of using Iterators")
cars = ["Aston", "Audi", "Maruti"]

i = 0
while(i < len(cars)):
    print(cars[i])
    i += 1


print("\nUsing for in/each loop")

cars = ["Aston", "Audi", "Maruti"]

for x in cars:
    print(x)

print("\nUsing Range Function")

cars = ["Aston", "Audi", "Maruti"]

for i in range(len(cars)):
    print(cars[i])

print("\nUsing enumerate")
cars = ["Aston", "Audi", "Maruti"]

for i, x in enumerate(cars):
    print(i,x)

cars = ["Aston", "Audi", "Maruti"]

for x in enumerate(cars):
    print(x[0], x[1])

cars = ["Aston" , "Audi", "McLaren "]
for x in enumerate(cars, start=1):
    print (x[0], x[1])

