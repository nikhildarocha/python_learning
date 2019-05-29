import math

def getFloat():
    result = float(input("Enter a number : "))
    return result


def Main():
    print("Getting started ")
    output = math.fabs(getFloat())
    print(output)



if __name__=="__main__":
    Main()

