# expenses = [10.5, 8, 5, 15, 20, 5, 3]

# sum = 0

# for expense in expenses:
#     sum += expense

# print(sum)

# print("You spent $", sum, " on lunch this week.", sep='')


# total = sum(expenses)
# print("You spent $", total, " on lunch this week.", sep='')

# for i in range(7):
#     print(i)



# total = 0
# expenses = []

# for i in range(7):
#     expenses.append(float(input("Enter an expenses: ")))

# total = sum(expenses)
# print("You spent $", total, " on lunch this week.", sep='')


expenses = []
num_expense = int(input("Enter a number of expenses"))
for i in range(num_expense):
    expenses.append(float(input("Enter an expense: ")))

total = sum(expenses)
print("You spent $", total, " on lunch this week.", sep='')






