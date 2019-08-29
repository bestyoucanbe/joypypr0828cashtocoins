# Now do the reverse. Convert the dollar amount into the coins that make up that dollar amount. The final result is an object with the correct number of quarters, dimes, nickels, and pennies.

# dollarAmount = 8.69

# piggyBank = {
#     "pennies": 0,
#     "nickels": 0,
#     "dimes": 0,
#     "quarters": 0
# }

# # Your magic Python code here
# That should produce the following output.

# >> > print(piggyBank)
# {'quarters': 34, 'nickels': 1, 'dimes': 1, 'pennies': 4}

# dollarAmount_including_cents = 8.69

dollarAmount_including_cents = 8.99
# ----------------------------------
number_of_quarters = (dollarAmount_including_cents / 0.25)
# remove if there is a fraction portion of the result using int
number_of_quarters = int(number_of_quarters)

amount_leftover_after_quarters = (dollarAmount_including_cents % 0.25)

# use round to get a useable value after the calculation (in case the calculation produces a decimal number that exceeds 2 decimal points)
amount_leftover_after_quarters = round(amount_leftover_after_quarters, 2)
# ------------------------------------
number_of_dimes = amount_leftover_after_quarters / 0.10

number_of_dimes = int(number_of_dimes)

amount_after_dimes = amount_leftover_after_quarters - (number_of_dimes * 0.10)

amount_after_dimes = round(amount_after_dimes, 2)
# ------------------------------------
number_of_nickels = amount_after_dimes / 0.05

number_of_nickels = int(number_of_nickels)

amount_after_nickels = amount_after_dimes - (number_of_nickels * 0.05)

amount_after_nickels = round(amount_after_nickels, 2)
# ------------------------------------
number_of_pennies = amount_after_nickels / 0.01

number_of_pennies = int(number_of_pennies)

amount_after_pennies = amount_after_nickels - (number_of_pennies * 0.01)

amount_after_pennies = round(amount_after_pennies, 2)
# ------------------------------------
piggybank = {
    "quarters":  number_of_quarters,
    "dimes":  number_of_dimes,
    "nickels":  number_of_nickels,
    "pennies":  number_of_pennies
}

print(f'Total Amount in Piggybank-->${dollarAmount_including_cents}')
print(f'My Piggybank-->{piggybank}')
