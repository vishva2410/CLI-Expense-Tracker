import exp
from datetime import datetime

def menu():
    while True:
        print("\nExpense Tracker Menu:")
        print("1. Add Expense")
        print("2. View Expenses")
        print("3. Delete Expense")
        print("4. Total Expenses")
        print("5. Category Summary")
        print("6₹. Exit")

        ch = input('Enter ur choice:')
        if ch == '1':
            date = input("Enter date (dd-mm-yyyy): ")
            category = input("Enter category: ")
            amount = float(input("Enter amount: "))
            description = input("Enter description: ")
            exp.add_exp(date, category, amount, description)
            print("Expense added successfully.")
        elif ch == '2':
            expenses = exp.view_expenses()
            for expense in expenses:
                print(expense)
        elif ch == '3':
            expense_id = int(input("Enter expense ID to delete: "))
            exp.delete_expense(expense_id)
            print("Expense deleted successfully.")
        elif ch == '4':
            total = exp.total_expenses()
            print(f"Total Expenses: {total}")
        elif ch == '5':
            summary = exp.category_summary()
            for category, total in summary:
                print(f"{category}: {total}")
        elif ch == '6':     
            print("Exiting...")
            break   
menu()
