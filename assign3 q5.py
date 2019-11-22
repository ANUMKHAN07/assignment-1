lst = []
val = input("Enter values in list separated by comma ")
lst = [int(x) for x in val.split(",")]
lst.sort()
for i in range (len (lst)-1):
    if lst[i] == lst[i+1]:
        print("The duplicate value is :",lst[i])