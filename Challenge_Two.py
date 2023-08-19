#define a function that checks if exactly two out of the three values given is positive
def positive_Values(x, y, z):
    #initializes a counter for the values
    positive_count = 0

#checks if the value and increment the counter is it is positive
    if x > 0:
        positive_count += 1
    if y > 0:
        positive_count += 1
    if z > 0:
        positive_count += 1

#returns True is exactly two numbers are positive otherwise returns False
    if positive_count == 2 and (x == 0 or y == 0 or z == 0):
        return True
    else:
        return False

try:
#read the three numbers from the user
    x = int(input("Enter your first number: "))
    y = int(input("Enter your second number: "))
    z = int(input("Enter your third number: "))
except ValueError:
    print("Please enter a valid number!")
else:
#calls the function positive_Values to check if exactly two numbers are positive and prints the results
    result = positive_Values(x,y,z)
    print("Results:", result)