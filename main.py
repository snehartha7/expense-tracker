import time

expenses = []
prices = []

def add_expense(expense, price):
    expenses.append(expense)
    prices.append(price)
    print(f"Added expense: {expense} - ${price:.2f}")

def view_expenses():
    if not expenses:
        print("No expenses recorded.")
        return
    print("Expenses:")
    for expense, price in zip(expenses, prices):
        print(f"{expense}: ${price:.2f}")
    
def total_expenses():
    total = sum(prices)
    print(f"Total expenses: ${total:.2f}")

def clear_expenses():
    expenses.clear()
    prices.clear()
    print("All expenses cleared.")

def delete_expense(index):
    if 0 <= index < len(expenses):
        removed_expense = expenses.pop(index)
        removed_price = prices.pop(index)
        print(f"Deleted expense: {removed_expense} - ${removed_price:.2f}")
    else:
        print("Invalid index. No expense deleted.")
def main():
    while True:
        print("\nExpense Tracker")
        print("1. Add Expense")
        print("2. View Expenses")
        print("3. Total Expenses")
        print("4. Clear Expenses")
        print("5. Delete Expense")
        print("6. Exit")
        
        choice = input("Choose an option: ")
        
        if choice == '1':
            expense = input("Enter expense description: ")
            price = float(input("Enter expense amount: "))
            add_expense(expense, price)
        elif choice == '2':
            view_expenses()
        elif choice == '3':
            total_expenses()
        elif choice == '4':
            clear_expenses()
        elif choice == '5':
            view_expenses()
            number = int(input("Enter the index of the expense to delete: "))
            index = number - 1
            delete_expense(index)
        elif choice == '6':
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please try again.")
        
        time.sleep(1)

main()