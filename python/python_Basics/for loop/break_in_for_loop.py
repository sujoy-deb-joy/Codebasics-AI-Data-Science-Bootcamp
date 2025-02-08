monthly_sales = [42, 38, 33, 38, 40, 45]

thresold = 35
for sales_amount in monthly_sales:
    if sales_amount < thresold:
        print(f"Sales amount {sales_amount} is below the thresold")
        break
    else:
        print(f"Sale amount {sales_amount} is above the thresold")

monthly_sales = [42, 38, 33, 38, 40, 45]
months = ["Jan", "Feb", "March", "April", "May", "June"]
# Loop through the list of months and print the corresponding sales amount
for month, sales_amount in zip(months, monthly_sales):
    if sales_amount < thresold:
        print(f"Sales amount {sales_amount} in {month} is below the thresold")
        # break
        continue
    else:
        print(f"Sale amount {sales_amount} in {month} is above the thresold")
    