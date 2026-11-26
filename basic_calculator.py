try:
    a = float(input("enter first number:"))
    b = float(input("enter second number:"))

    print("addition:",a+b)
    print("substraction:",a-b)
    print("multiplication",a*b)

    if b == 0:
        print("division not possible")

    else:
        print("division:",a/b)
    
    
    print("power",a**b)
    print("modulus",a%b)

except:
    print("invalid input")    