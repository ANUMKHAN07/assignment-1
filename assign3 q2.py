string = input("Enter list values separated by comma : ")  
res = [int(i) for i in string.split(",") if i.isdigit()] 
print("The numbers list is : ",str(res))