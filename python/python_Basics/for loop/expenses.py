# without for loop
expenses = [1200, 1300, 1500, 1700]
total_expense = expenses[0] + expenses[1] + expenses[2] + expenses[3]
print("Total expense:", total_expense)

# with for loop
total_expense = 0
for expense in expenses:
    total_expense += expense
print("Total expense:", total_expense)

# range function
total_expense = 0
for item in range(len(expenses)):
    expense = expenses[item]
    print(f'Month {item+1}, Expense: {expense}')
    total_expense += expense

print("Total expense:", total_expense)

# enumerate function
total_expense = 0
for item, expense in enumerate(expenses):
    print(f'Month {item+1}, Expense: {expense}')
    total_expense += expense
print("Total expense:", total_expense)