user_dict = {}
sum = 0
n = int(input("Enter number of keys to add :"))
for i in range(n) :
    string = input('Enter key value pairs')
    (key,value) = string.split()
    user_dict[key] = value
    sum = sum + int(value)
print("The total sum key values is :",sum)