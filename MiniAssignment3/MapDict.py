Keys = ["Ten", "Twenty", "Thirty"]
Value = [10,20,30]

dictionary= dict()

for i in range(len(Keys)):
    dictionary.setdefault(Keys[i],[]).append(Value[i])

print("Keys : ",Keys)
print("Value : ",Value)
print("Dictionary : ",dictionary)