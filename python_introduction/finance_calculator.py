user1 = int(input("Enter your monthly income: "))
user2 = int(input("Enter your total monthly expenses: "))
savings = user1 - user2
print(f"Your monthly savings are {savings}.")
projected_savings = int(savings * 12 + (savings * 12 * 0.05))
print(
    f"Projected savings after one year, with interest, is: {projected_savings}.")
