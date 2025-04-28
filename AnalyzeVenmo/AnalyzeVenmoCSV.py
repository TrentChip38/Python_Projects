import os
import csv
import pandas as pd
from collections import defaultdict

transactions_folder = "Transactions"

total_spent = defaultdict(float)
individual_transactions = defaultdict(list)

for filename in os.listdir(transactions_folder):
    if filename.endswith(".csv"):
        filepath = os.path.join(transactions_folder, filename)
        
        # Read skipping 2 junk rows
        df = pd.read_csv(filepath, skiprows=2)
        
        for _, row in df.iterrows():
            if 'From' in row and 'Amount (total)' in row:
                name = row['From']
                amount = row['Amount (total)']
                
                if pd.notna(name) and pd.notna(amount):
                    try:
                        # Clean the amount string
                        amount = str(amount).replace('$', '').replace('+', '').replace(',', '').strip()
                        amount = float(amount)
                        
                        total_spent[name] += amount
                        individual_transactions[name].append(amount)
                    except ValueError:
                        print(f"Warning: Skipped invalid amount '{amount}' for {name} in {filename}")

# Top spenders
top_spenders = sorted(total_spent.items(), key=lambda x: x[1], reverse=True)[:100]

print("\nTop 100 Spenders and their top payments:")
for i, (name, total) in enumerate(top_spenders, 1):
    print(f"{i}. {name}: ${total:.2f}")
    #top_5 = sorted(individual_transactions[name], reverse=True)[:5]
    #print(f"   Top 5 Transactions: {', '.join(f'${amt:.2f}' for amt in top_5)}")

top_spenders = sorted(total_spent.items(), key=lambda x: x[1], reverse=True)[:10]
print("\nTop 10 Spenders:")
for i, (name, total) in enumerate(top_spenders, 1):
    print(f"{i}. {name}: ${total:.2f}")
    top_5 = sorted(individual_transactions[name], reverse=True)[:5]
    print(f"   Top 5 Transactions: {', '.join(f'${amt:.2f}' for amt in top_5)}")

for i, (name, total) in enumerate(top_spenders, 1):
    print(f"{i}. {name}: ${total:.2f}")

# Save results
output_rows = []
for name, total in top_spenders:
    top_5 = sorted(individual_transactions[name], reverse=True)[:5]
    output_rows.append({
        'Name': name,
        'Total Spent': total,
        'Top Transaction 1': top_5[0] if len(top_5) > 0 else '',
        'Top Transaction 2': top_5[1] if len(top_5) > 1 else '',
        'Top Transaction 3': top_5[2] if len(top_5) > 2 else '',
        'Top Transaction 4': top_5[3] if len(top_5) > 3 else '',
        'Top Transaction 5': top_5[4] if len(top_5) > 4 else '',
    })

df_out = pd.DataFrame(output_rows)
df_out.to_csv("Top_Spenders.csv", index=False)
df_out.to_excel("Top_Spenders.xlsx", index=False)

print("\nSaved results to 'Top_Spenders.csv' and 'Top_Spenders.xlsx'.")
