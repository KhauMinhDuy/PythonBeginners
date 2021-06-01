# Get the loan detail
money_owed = float(input("How much money do you owe, dollars: ")) #50000
apr = float(input("What is the annual percentage rate: ")) #3
payment = float(input("What will you month payment be, in dollars: ")) #1000
month = int(input("How many months do you want see results for: ")) #24

# Divide apr by 100 to make it a percent, then divide by 12 to make monthly
monthly_rate = apr/100/12

for i in range(month):
    # Add in interect
    interect_paid = money_owed * monthly_rate
    money_owed += interect_paid

    if money_owed - payment < 0:
        print("The last payment is", money_owed)
        print("You paid off the loan is", i+1, "months")
        break

    # make payment
    money_owed -= payment


    # print the result after this month
    print("Paid", payment, "of which", interect_paid, "was interect", end=" ")
    print("Now I owe", money_owed)