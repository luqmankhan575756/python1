# Billing & Invoice System in Python

print("----- Welcome to Billing System -----")

items = []  # To store item names
prices = [] # To store item prices
qtys = []   # To store quantities

tax_rate = 0.05  # 5% tax

while True:
    item = input("Enter item name (or type 'done' to finish): ")
    if item.lower() == "done":
        break

    qty = int(input("Enter quantity: "))
    price = float(input("Enter price per item: "))

    items.append(item)
    qtys.append(qty)
    prices.append(price)

# Display Invoice
print("\n=========== INVOICE ===========")
total = 0

for i in range(len(items)):
    cost = prices[i] * qtys[i]
    total += cost
    print(f"{items[i]}  x{qtys[i]}  = Rs {cost}")

tax = total * tax_rate
grand_total = total + tax

print("--------------------------------")
print(f"Subtotal: Rs {total}")
print(f"Tax (5%): Rs {tax:.2f}")
print(f"Total Bill: Rs {grand_total:.2f}")
print("======= Thank You! Visit Again =======")
