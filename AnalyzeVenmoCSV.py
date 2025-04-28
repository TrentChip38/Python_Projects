import os
import csv
from collections import defaultdict

# Path to the Transactions folder
transactions_folder = "Transactions"

# Data structures
total_spent = defaultdict(float)   # Person -> total amount
individual_transactions = defaultdict(list)  # Person -> list of all their amounts

# Read all CSV files in the Transactions folder
for filename in os.listdir(transactions_folder):
    if filename.endswith(".csv"):
        filepath = os.path.join(transactions_folder, filename)
        with open(filepath, mode='r', encoding='utf-8-sig') as file:
            reader = csv.DictReader(file)
            for row in reader:
                # Assuming 'Name' and 'Amount' are the column headers
                name = row.get('Name') or row.get('name')
                amount = row.get('Amount') or row.get('amount')
                
                if name and amount:
                    try:
                        amount = float(amount)
                        total_spent[name] += amount
                        individual_transactions[name].append(amount)
                    except ValueError:
                        print(f"Warning: Skipped invalid amount '{amount}' for {name} in {filename}")

# Analyze the results
# Find top 10 spenders
top_spenders = sorted(total_spent.items(), key=lambda x: x[1], reverse=True)[:10]

print("Top 10 Spenders:")
for i, (name, total) in enumerate(top_spenders, 1):
    print(f"{i}. {name}: ${total:.2f}")
    
    # Top 5 biggest transactions for this person
    top_5_transactions = sorted(individual_transactions[name], reverse=True)[:5]
    print(f"   Top 5 Transactions: {', '.join(f'${amt:.2f}' for amt in top_5_transactions)}")
