#BMI - Body Mass Index calculator 

print("Welcome to Body Mass Index (BMI) calculator.\n")
print("BMI = weight / (height * height))\n")
height_input = input("Your height in m: ")
weight_input = input("Your weight in kg: ")

height = float(height_input)
weight = int(weight_input)

bmi = int(weight / (height ** 2))

print (f"\nYour BMI is: {bmi}\n")