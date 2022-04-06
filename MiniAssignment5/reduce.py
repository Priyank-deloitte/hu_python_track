from functools import reduce

lst = [2, 4, 5, 9, 15, 4]

multiply = reduce(lambda a, b: a * b,  lst)

print("List : ", lst)
print("Last result : ", multiply)
