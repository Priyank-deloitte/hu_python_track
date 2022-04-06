lst1 = ["Alaska", "Alabama", "Arizona", "Arkansas", "Colorado", "Montana", "Nevada"]

countOfa = list(map(lambda x: x.count("a"), lst1))
countOfA = list(map(lambda x: x.count("A"), lst1))

print("List : ", lst1)
print("Count list of 'a' : ", countOfa)
print("Count list of 'A' : ", countOfA)
