# write a decorator which will take a function and execute it twice.

def twice_multiply(func):
    def inner(num1, num2):
        print(num1 * num2)
        return func(num1, num2)
    return inner


@twice_multiply
def multiply(num1, num2):
    print(num1 * num2)


num1 = int(input("Number 1 : "))
num2 = int(input("Number 2 : "))
multiply(num1, num2)

