a = input("Type the first number: ")
b = input("Type the second number: ")
math = input("Do you want to add or subtract? Type + or -: ")

a = int(a)
b = int(b)

if math == ("+"):
    c = a + b
    print("You chose to add the two numbers together. Your result is:", c)
elif math == ("-"):
    c = a - b
    print("You chose to subtract the second number from the first. Your result is:", c)
else:
    print("You did not type + or -. Please try again using one of the two options.")