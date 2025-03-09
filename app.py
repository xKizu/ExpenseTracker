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
    expenses = load_expenses()
    expense = {
        "id": len(expenses) + 1,
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

def delete_expense(id):
    expenses = load_expenses()
    expenses = [expense for expense in expenses if expense["id"] != id]
    save_expenses(expenses)
    print(f"Expense of ID {id} deleted successfully")

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