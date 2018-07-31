# calculate and interpret BMI
# input
w=float(input("plz enter your weight in kg"))
h=float(input("plz enter your height in meters"))
bmi=w/h**2
# interpretation of BMI
if bmi<=18.5:
    print("Underweight")
elif bmi<=24.9:
    print("Normal")
elif bmi<=29.9:
    print("overweight")
else:
    print("Obese")