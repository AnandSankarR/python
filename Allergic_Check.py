# Create Allergy check code
# [ ] get input for input_test variable
input_test = input("input somethings eaten in last 24 hrs:").lower()

# [ ] print "True" message if "dairy" is in the input or False message if not
print("It is","diary" in input_test, "that",'"'+input_test.lower()+'"','contains "diary"')

# [ ] print True message if "nuts" is in the input or False if not
print("It is","nuts" in input_test, "that",'"'+input_test.lower()+'"','contains "nuts"')

# [ ] Challenge: Check if "seafood" is in the input - print message
print("It is","seafood" in input_test, "that",'"'+input_test.lower()+'"','contains "seafood"')

# [ ] Challenge: Check if "chocolate" is in the input - print message
print("It is","chocolate" in input_test, "that",'"'+input_test.lower()+'"','contains "chocolate"')