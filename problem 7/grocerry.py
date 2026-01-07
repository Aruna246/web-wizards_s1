items = {
    "Rice": 50,
    "Wheat": 30,
    "Sugar": 40
}

def generate_bill():
    total = 0
    bill = {}
    while True:
        item = input("Enter item name: ")
        if item.lower() == "ok":
            break
        if item in items:
            quantity = int(input("Enter quantity: "))
            bill[item] = quantity
            total += items[item] * quantity
        else:
            print("Item not found.")
    print("Bill:")
    for item, quantity in bill.items():
        print(f"{item}: {items[item]} x {quantity} = {items[item] * quantity}")
    print(f"Total: {total}")

if __name__ == "__main__":
    generate_bill()
