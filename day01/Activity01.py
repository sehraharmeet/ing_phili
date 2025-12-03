#1. Write a Python program that asks the user to enter 10 numbers (one by one).
#lassify each number as:
#Positive even
#Positive odd
#Negative
#Zero
def info_decorator(func):
    def wrapper(*args,**kwargs):
        print("WELCOME FROM HARMEET")
        result=func(*args,**kwargs)
        print("Thanks FROM HARMEET")
        return result
    return wrapper

@info_decorator
def MyFunction(*no):
    for i in no:
        num = i

        if num > 0:
            if num % 2 == 0:
                print(num, "is Positive Even")
            else:
                print(num, "is Positive Odd")

        elif num < 0:
            print(num, "is Negative")

        else:
            print(num, "is Zero")


#MyFunction()