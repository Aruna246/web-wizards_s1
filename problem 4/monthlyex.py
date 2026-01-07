expenses = {}
def add_expense():
    category = input("Enter category:")
    amount = float(input("Enter amount:"))
    if category in expenses:
        expenses[category] += amount
    else:
        expenses[category] = amount
def calculate_total():
    return sum(expenses.values())
def find_highest_category():
    return max(expenses, key=expenses.get)
def main():
    while True:
        choice = input("Enter your choice:")
        if choice == "1":
            add_expense()
        elif choice == "2":
            print(f"Total Expense: {calculate_total():.2f}")
        elif choice == "3":
            highest_category = find_highest_category()
            print(f"Highest Spending Category: {highest_category} ({expenses[highest_category]:.2f})")
        else:
            print("Invalid choice.")
if __name__ == "__main__":
    main()
