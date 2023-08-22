# mortgage.py
#
# Exercise 1.8 -- Extra Payments

principal = 500000.0
rate = 0.05
payment = 2684.11
total_paid = 0.0
extra = 1000
months_elapsed = 1

while principal > 0:
    if months_elapsed < 13:
        total_paid = total_paid + payment + 1000
        principal = principal * (1+rate/12) - (payment + 1000)
    else:
        total_paid = total_paid + payment
        principal = principal * (1+rate/12) - payment
    months_elapsed = months_elapsed + 1

print('Total paid', round(total_paid, 7))
print('Months elapsed', months_elapsed - 1)
print()

# Exercise 1.9 -- Extra Payments Calculator
# Modify the program so that extra payment information can be more generally handled. Make it so that the user can set these variables:
#
# extra_payment_start_month = 61
# extra_payment_end_month = 108
# extra_payment = 1000

principal = 500000.0
rate = 0.05
payment = 2684.11
total_paid = 0.0
extra = 1000
months_elapsed = 1
extra_payment_start_month = 61
extra_payment_end_month = 108
extra_payment = 1000

while principal > 0:
    if months_elapsed > extra_payment_start_month - 1 and months_elapsed < extra_payment_end_month + 1:
        total_paid = total_paid + payment + extra_payment
        principal = principal * (1+rate/12) - (payment + extra_payment)
    else:
        total_paid = total_paid + payment
        principal = principal * (1+rate/12) - payment
    months_elapsed = months_elapsed + 1

print('[Extra Payment Calculator] Total paid', round(total_paid, 7))
print('[Extra Payment Calculator] Months elapsed', months_elapsed - 1)
print()

# Exercise 1.10 -- Making a table
# Modify the program to print out a table showing the month, total paid so far, and the remaining principal.

principal = 500000.0
rate = 0.05
payment = 2684.11
total_paid = 0.0
extra = 1000
months_elapsed = 1
extra_payment_start_month = 61
extra_payment_end_month = 108
extra_payment = 1000

while principal > 0:
    if months_elapsed >= extra_payment_start_month and months_elapsed <= extra_payment_end_month:
        total_paid = total_paid + payment + extra_payment
        principal = principal * (1+rate/12) - (payment + extra_payment)
    else:
        total_paid = total_paid + payment
        principal = principal * (1+rate/12) - payment
    print(months_elapsed, round(total_paid,7), round(principal,2))
    months_elapsed = months_elapsed + 1
print('[Table] Total paid', round(total_paid, 7))
print('[Table] Months elapsed', months_elapsed - 1)
print()

# Exercise 1.11 -- Bonus
# Fix the program to correct for the overpayment that occurs in the last month.

principal = 500000.0
rate = 0.05
payment = 2684.11
total_paid = 0.0
extra = 1000
months_elapsed = 1
extra_payment_start_month = 61
extra_payment_end_month = 108
extra_payment = 1000

while principal > 0:
    if months_elapsed >= extra_payment_start_month and months_elapsed <= extra_payment_end_month:
        total_paid = total_paid + payment + extra_payment
        principal = principal * (1+rate/12) - (payment + extra_payment)
    else:
        total_paid = total_paid + payment
        principal = principal * (1+rate/12) - payment
    if principal < 0:
            total_paid = total_paid - abs(principal);
            principal = 0
    months_elapsed = months_elapsed + 1

print('[Bonus] Total paid', round(total_paid, 2))
print('[Bonus] Months elapsed', months_elapsed - 1)
print()

# Exercise 1.17 -- f-string
# Modify the mortgage.py program from Exercise 1.10 to create its output using f-strings. Try to make it so that output is nicely aligned.

principal = 500000.0
rate = 0.05
payment = 2684.11
total_paid = 0.0
extra = 1000
months_elapsed = 1
extra_payment_start_month = 61
extra_payment_end_month = 108
extra_payment = 1000

while principal > 0:
    if months_elapsed >= extra_payment_start_month and months_elapsed <= extra_payment_end_month:
        total_paid = total_paid + payment + extra_payment
        principal = principal * (1+rate/12) - (payment + extra_payment)
    else:
        total_paid = total_paid + payment
        principal = principal * (1+rate/12) - payment
    print(f'{months_elapsed}, {round(total_paid,7)}, {round(principal,2)}')
    months_elapsed = months_elapsed + 1
print()
print('[Table] Total paid', round(total_paid, 7))
print('[Table] Months elapsed', months_elapsed - 1)
print()