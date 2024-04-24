num1 = int (input("Enter first number: "))
num2 = int (input ("Enter second number: "))
print ("Add or multiply?")
ans = input("+ or *?")
if ans =='+':
    sum = num1+num2
    print("Total is ", sum)
else:
    product = num1*num2
    print("Multiplied value is ", product)