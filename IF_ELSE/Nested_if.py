height=int(input("enter the height in cm: "))
if height>=120:
    print("U are eligible to ride")
    age=int(input("Enter the value of age: "))
    if age<18:
        print("You have to pay 7rs")
    else:
        print("You have to pay 18rs")
else:
    print("u are not eligible for the ride")    