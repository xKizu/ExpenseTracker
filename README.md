# Expense Tracker 

Simple Expense Tracker 


# Usage
```sh
 python expense-tracker.py add --description "Lunch" --amount 20
 Expense added successfully (ID: 1)

 python expense-tracker.py add --description "Dinner" --amount 10
 Expense added successfully (ID: 2)

 python expense-tracker.py list
 ID  Date       Description  Amount
 1   2024-08-06  Lunch        $20
 2   2024-08-06  Dinner       $10

 python expense-tracker.py summary
 Total expenses: $30

 python expense-tracker.py delete --id 2
 Expense deleted successfully

 python expense-tracker.py summary
 Total expenses: $20

```
