
#Write a program to check whether the given values have boolean values or not.

values = int(input("Enter a number between 1 and 10: "))

if values == 4 or values == 2:
    print("this is a boolean value")
else:
    print("not a boolean value")



# task 2

# Write a Python program to show how the logical not operator is used to reverse conditions and check whether values are different.

num_1 = 10
num_2 = 3
if not(num_1 - num_2 == 7):
    print("The difference between num_1 and num_2 is NOT 7")
elif not(num_1 % num_2 == 0):
    print("The answer for num_1 and num_2 is NOT equal to 0")



# task 3
#Write a program to calculate the BMI of a person?

#BMI = weight (kg) ÷ [height (m)]²

weight = float(input("enter your weight in kg: "))
height = float(input("enter your height in m: "))

BMI = ((weight)/(height)**2)
print(BMI)
