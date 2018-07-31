# calculate the Euclidean distance between two data points
# input
x1=float(input("plz enter x1"))
x2=float(input("plz enter x2"))
y1=float(input("plz enter y1"))
y2=float(input("plz enter y2"))
# process
d=((x1-x2)**2+(y1-y2)**2)**0.5
# output
print(round(d,2))