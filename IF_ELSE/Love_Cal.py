print("Welcome to love calculator")
n1=input("Enter your name:  ")
n2=input("Enter your partner's name: ")
a=n1+n2
c=a.lower()
t=c.count("t")
r=c.count("r")
u=c.count("u")
e=c.count("e")
true=t+r+u+e
l=c.count("l")
o=c.count("o")
v=c.count("v")
e=c.count("e")
love=l+o+v+e

love_score=str(true)+str(love)
print("your love pertcent is : ",love_score)
