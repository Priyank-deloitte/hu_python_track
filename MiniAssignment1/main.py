class StringClass:
    def __init__(self):
        self.str1=""

    def get_string(self):
        self.str1 = input("Enter the String :")

    def LengthOfString(self):
        return len(self.str1)

    def StringToList(self):
        return list(self.str1)

str1 = StringClass()
str1.get_string()
print(str1.LengthOfString())
print(str1.StringToList())