lst1 = [-1000, 500, -600, 700, 5000, -90000, -17500]
result = list(filter(lambda x: x < 0, lst1))

positiveList = []
for i in range(len(result)):
    val = abs(result[i])
    positiveList.append(val)

print("Original List : ", lst1)
print("List of negative numbers converted to positive : ", positiveList)

