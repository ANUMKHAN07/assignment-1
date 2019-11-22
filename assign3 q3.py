user_dict = {}
n = int(input("Enter number of keys to add :"))
for i in range(n) :
    string = input('Enter key value pairs')
    (key,value) = string.split()
    user_dict[key] = value
print("The user entered key:values are : ",user_dict)
