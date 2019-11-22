a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
print("Select on of the following operation:\n + for addition\n - for subtraction\n * for multiplication\n / for division\n ** for power")
c = input("Enter operator to use:")
if c == '+':
    ans = a+b
    print("The answer of a",c,"b is =",ans)
elif c == '-':
    ans = a-b
    print("The answer of a",c,"b is =",ans)
elif c == '*':
    ans = a*b
    print("The answer of a",c,"b is =",ans)
elif c == '/':
    ans = a/b
    print("The answer of a",c,"b is =",ans)
elif c == '**':
    ans = a**b
    print("The answer of a",c,"b is =",ans)
else:
    print("Invalid input")