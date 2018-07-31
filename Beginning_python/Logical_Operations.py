# logical operators
n=float(input("plz enter a number"))
if n%2==0 and n%3==0:
    print("Case1")
if n%2==0 or n%3==0:
    print("Case2")
if (n%2==0 and n%3!=0) or (n%2!=0 and n%3==0):
    print("Case3")

