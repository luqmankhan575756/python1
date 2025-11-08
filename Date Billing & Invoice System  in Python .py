import datetime

# Billing & Invoice System with more features

print("----- Welcome to Billing System -----")

items = []
prices = []
qtys = []

# Invoice number and date
invoice_no = datetime.datetime.now().strftime("%Y%m%d%H%M%S")
date = datetime.datetime.now().strftime("%d-%m-%Y %H:%M")

# Choose Tax Rate
print("\nSelect Tax Rate:")
print("1) 0%")
print("2) 5%")
print("3) 10%")
print("4) 18%")

choice = int(input("Enter tax option (1-4): "))

if choice == 1:
    tax_rate = 0.00
elif choice == 2:
    tax_rate = 0.05
elif choice == 3:
    tax_rate = 0.10
elif choice == 4:
    tax_rate = 0.18
else:
    print("Invalid choice! Default 5% tax applied.")
    tax_rate = 0.05

# Add Items
while True:
    item = input("Enter item name (or type 'done' to finish): ")
    if item.lower() == "done":
        break

    qty = int(input("Enter quantity: "))
    price = float(input("Enter price per item: "))

    items.append(item)
    qtys.append(qty)
    prices.append(price)

# Discount Option
discount = float(input("Enter discount percentage (e.g., 10 for 10%): "))
discount_rate = discount / 100

# Display Invoice
print("\n=========== INVOICE ===========")
print(f"Invoice No: {invoice_no}")
print(f"Date: {date}")
print("--------------------------------")

total = 0
for i in range(len(items)):
    cost = prices[i] * qtys[i]
    total += cost
    print(f"{items[i]}  x{qtys[i]}  = Rs {cost}")

discount_amount = total * discount_rate
tax = (total - discount_amount) * tax_rate
grand_total = total - discount_amount + tax

print("--------------------------------")
print(f"Subtotal: Rs {total:.2f}")
print(f"Discount ({discount}%): -Rs {discount_amount:.2f}")
print(f"Tax ({tax_rate*100}%): Rs {tax:.2f}")
print("--------------------------------")
print(f"Total Bill: Rs {grand_total:.2f}")
print("======= Thank You! Visit Again =======")
