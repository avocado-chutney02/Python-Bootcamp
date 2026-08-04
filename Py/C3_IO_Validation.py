#Concept Input/Output Validation

name = input("Enter your name: ")
height = float(input("Enter your height: "))
weight = float(input("Enter your weight: ")) #Convert to float

#Input validation

while True:
    try:
        age = int(input("Enter your age: "))
        if age > 0:
            break
        else:
            print("Age must be positive!")
    except ValueError:
        print("Please enter a valid number!")

#Output Validation

print(f"Hello, {name}!")
print(f"You are {age} years old and {height} cm tall and your weight is {weight} kg.")

#Exercise 1: Create a simple calculator that takes two number and an operation from user


