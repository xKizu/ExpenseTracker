import argparse
import json
import os
from datetime import datetime

data_file = "expenses.json"

if not os.path.exists(data_file):
    with open(data_file, "w") as file:
        json.dump([], file)

def save_expenses(expenses):
    with open(data_file, "w") as file:
        json.dump(expenses, file)

def load_expenses():
    with open(data_file, "r") as file:
        return json.load(file)


def add_expense(description, amount):
    if amount <= 0:
        print("Amount must be [bold green]greater[/bold green] than 0.")
        return
    
    try:
        amount = float(amount)
        if round(amount, 2) != amount:
            raise ValueError("Amount must have at most two decimal places.")
    except ValueError as e:
        print(f"[bold red]{e}[/bold red]")
        return
    
    expenses = load_expenses()

    if len(expenses) == 0:
        expense_id = 1
    else:
        expense_id = expenses[-1]['id'] + 1

    expense = {
        "id": expense_id,
        "description": description,
        "amount": amount,
        "date": datetime.now().strftime("%Y-%m-%d")
    }
    expenses.append(expense)
    save_expenses(expenses)
    print(f"Expense of ID {expense['id']} added successfully")

def list_expenses():
    expenses = load_expenses()
    if expenses:
        print("# ID  Date       Description  Amount")
    else:
        print("No expenses found")
    for expense in expenses:
        print(f"# {expense['id']}   {expense['date']}  {expense['description']}        ${expense['amount']}")

def delete_expense(expense_id):
    expenses = load_expenses()
    if not expenses:
        print("No expenses found.")

    if not any(expense['id'] == expense_id for expense in expenses):
        print(f"Expense with ID: {expense_id} not found.")
        return
    expenses = [expense for expense in expenses if expense["id"] != expense_id]
    save_expenses(expenses)
    print(f"Expense of ID {expense_id} deleted successfully")

def update_expense(id, description, amount):
    expenses = load_expenses()
    for expense in expenses:
        if expense["id"] == id:
            if description:
                expense["description"] = description
            if amount:
                expense["amount"] = amount
            break
    save_expenses(expenses)
    print(f"Expense of ID {id} updated successfully")

def summarize_expenses(month):
    expenses = load_expenses()
    total = 0
    if month:
        for expense in expenses:
            if int(expense["date"].split("-")[1]) == month:
                total += expense["amount"]
    else:
        total = sum(expense["amount"] for expense in expenses)
    print(f"Total expenses for the month: ${total}")



def main():
    parser = argparse.ArgumentParser(description="Expense Tracker Application")
    subparsers = parser.add_subparsers(dest="command")

    add_parser = subparsers.add_parser("add")
    add_parser.add_argument("--description", required=True, help="Description of the expense")
    add_parser.add_argument("--amount", required=True, type=float, help="Amount of the expense")

    list_parser = subparsers.add_parser("list", help="List all expenses")

    delete_parser = subparsers.add_parser("delete")
    delete_parser.add_argument("--id", required=True, type=int, help="ID of the expense to delete")

    summary_parser = subparsers.add_parser("summary")
    summary_parser.add_argument("--month", type=int, help="Month for which to summarize expenses (1-12)")

    update_parser = subparsers.add_parser("update")
    update_parser.add_argument("--id", required=True, type=int, help="ID of the expense to update")
    update_parser.add_argument("--description", help="New description for the expense")
    update_parser.add_argument("--amount", type=float, help="New amount for the expense")

    args = parser.parse_args()

    if args.command == "add":
        add_expense(args.description, args.amount)
    elif args.command == "list":
        list_expenses()
    elif args.command == "delete":
        delete_expense(args.id)
    elif args.command == "update":
        update_expense(args.id, args.description, args.amount)
    elif args.command == "summary":
        summarize_expenses(args.month)
    else:
        parser.print_help()

























if __name__ == "__main__":
    main()
