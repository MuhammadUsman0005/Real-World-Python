def add_expense(expenses):
    name = input("Item name: ")
    amount = float(input("Enter amount: "))
    expenses.append({"name":name,"amount":amount})

def show_report(expenses):
    total = sum(item['amount'] for item in expenses)
    print("\n--- Expense Report ---")
    for i, item in enumerate(expenses,1):
        print(f"{i}. {item['name']}: ${item['amount']:.2f}")
    print(f"TOTAL: ${total:.2f}")


expenses = []
while True:
    choice = input("\n1. Add expense\n2. Show report\n3. Quit\n> ")
    if choice == '1': add_expense(expenses)
    elif choice == '2': show_report(expenses)
    elif choice == '3': break
