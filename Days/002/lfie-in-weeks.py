#Life in weeks calculator

print("Welcome to life in weeks (till you are 90) calculator.\n")
age_input = input("What is your current age? ")

age = int(age_input)

years_remaining = 90 - age
days_remaining = years_remaining * 365
weeks_remaining = years_remaining * 65
months_remaining = years_remaining * 12

message = f"\nYou have {years_remaining} years or {months_remaining} months or {weeks_remaining} weeks or {days_remaining} days remaining.\n"
print(message)
