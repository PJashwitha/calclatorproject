a = int(input("enter a : "))
b = int(input("enter b : "))
operator = input("enter the input : ")
if operator=="+":
    print(a+b)
elif operator=="-" :
    print(a-b)
elif operator=="*"    :
    print(a*b)
elif operator=="/"    :
    print(a/b)
elif operator=="%"    :
    print(a%b)
else:
    print("enter valid operator")    