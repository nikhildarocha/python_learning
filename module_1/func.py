num = int(input("Enter number : "))

def calc():
    if(num > 10):
        print("You win")
    elif(num > 35):
        print("You are close to winning")
    else:
        print("You loose")

calc()