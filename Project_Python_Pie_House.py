# Project - Pie Shopping from Pie House

#Intialize Shopping status
shopping = "y"

# List of Pie purchase
pie_purchases = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

# list of pies
pie_list = ["Oreo", "Grasshopper", "Lemon Meringue", "Apple",
            "Banana Cream", "Shaker", "Pecan", "Pumpkin",
            "Chocolate Cream", "Strawberry-Rhubarb"]

# Welcome info
print(" Welcome to the Pie House !!! " + " Our Pie Menu Follows: ")

# While we are still shopping
while shopping == "y":

# show pie select prompt

    print("----------------------------------------------------------------------------------")

    print(" (1) Oreo , (2) Grasshopper ,(3) Lemon Meringue ,(4) Apple " +
      " (5) Banana Cream , (6) Shaker , (7) Pecan , (8) Pumpkin " +
      " (9) Chocolate Cream (10) Strawberry-Rhubarb ")

    pie_choice = input(" What would you like to purchase, please ??:")

# Add pie to the pie list by finding the matching index and adding one to its value
    pie_purchases[ int(pie_choice) - 1] = pie_purchases[ int(pie_choice) - 1] + 1

    print("----------------------------------------------------------------------------------")

# Inform the customer of the pie purchase
    print(" Great ! We will have your order " + pie_list[ int(pie_choice) - 1] + " Ready for you!!!!")

# providing exit option
    shopping = input("Would you like to make another purchase: (y)es or (n)o? ")

print("----------------------------------------------------------------------------------")

print(" Thank You for the visit!!!")

# count the purchases
print(" Total Pie Purchased:")

# Loop through the full pie list
for pie_index in range(len(pie_list)):
# Gather the count of each pie in the pie list and print them alongside the pies
    print(str(pie_purchases[pie_index]) + " " + str(pie_list[pie_index]))
