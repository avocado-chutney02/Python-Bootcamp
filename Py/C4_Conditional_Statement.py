#Concept Conditional Statement

#Example A: if-else: 2 conditions

age = int(input("Enter you're age: "))

if age >= 18:
    print("You are an adult.")
else:
    print("You are a minor.")

#Example B: if-elif-else: more than 2 conditions

score = int(input("Enter your score: "))

if score >= 90:
      grade = "A"
elif score >= 80:
    grade = "B"
elif score >= 70:
    grade = "C"
elif score >= 60:
    grade = "D"
else:
    grade = "F"

print(f"Your grade is: {grade}")

#Example C: and: both conditions must be True

user_age = 25 
has_license = True 







