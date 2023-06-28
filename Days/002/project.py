# Tip Calculator

print("Welcome to the tip calculator.\n")

bill_amt = float(input("What was the total bill? $ "))
tip_percent = int(input("What percentage tip would you like ot give? 10, 12, or 15? "))
total_bill = bill_amt * (1 + tip_percent / 100)
print(f"\nTotal bill with tip: $ {total_bill:.2f}\n")