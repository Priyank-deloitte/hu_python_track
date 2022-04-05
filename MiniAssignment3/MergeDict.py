def Merge(dict1 , dict2):
    return (dict1.update(dict2))


d1 = {'Ten': 10, 'Twenty': 20, 'Thirty': 30}
d2 = {'Thirty': 30, 'Fourty': 40, 'Fifty': 50}
print("Dictionary 1 : ",d1)
print("Dictionary 2 : ",d2)

Merge(d1 , d2)
print("Merged Dictionary : ",d1)