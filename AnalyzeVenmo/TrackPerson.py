import os
import pandas as pd
import matplotlib.pyplot as plt
from collections import defaultdict

# ========== Settings ==========

# Folder where all Venmo CSV files are
transactions_folder = "Transactions"

# People you want to track
people_to_track = ["Hassan Sher", "Trent Chipman", "Maggie Michelsen", "Benjamin Ginnett", ""]

# =================================

# Dictionary: person -> {month -> total spent}
spending_data = defaultdict(lambda: defaultdict(float))

# Read all CSVs
for filename in os.listdir(transactions_folder):
    if filename.endswith(".csv") and filename.startswith("VenmoStatement_"):
        # Extract month info from filename
        parts = filename.split("_")
        if len(parts) >= 2:
            month = parts[1].replace(".csv", "")
        
            filepath = os.path.join(transactions_folder, filename)
            df = pd.read_csv(filepath, skiprows=2)

            for _, row in df.iterrows():
                if 'From' in row and 'Amount (total)' in row:
                    name = row['From']
                    amount = row['Amount (total)']

                    if pd.notna(name) and pd.notna(amount):
                        try:
                            amount = str(amount).replace('$', '').replace('+', '').replace(',', '').strip()
                            amount = float(amount)

                            if name in people_to_track:
                                spending_data[name][month] += amount
                        except ValueError:
                            print(f"Warning: skipped invalid amount '{amount}' for {name} in {filename}")

# Turn into a nice DataFrame
months_sorted = sorted({month for person in spending_data.values() for month in person.keys()})
df_spending = pd.DataFrame(index=months_sorted)

for person in people_to_track:
    df_spending[person] = [spending_data[person].get(month, 0) for month in months_sorted]

# Save to CSV and Excel
df_spending.to_csv("People_Spending_By_Month.csv")
df_spending.to_excel("People_Spending_By_Month.xlsx")
print("\nSaved spending data to People_Spending_By_Month.csv and People_Spending_By_Month.xlsx!")

# Plot the data
plt.figure(figsize=(10, 6))
for person in people_to_track:
    plt.plot(df_spending.index, df_spending[person], marker='o', label=person)

plt.title("Monthly Spending per Person")
plt.xlabel("Month")
plt.ylabel("Total Spending ($)")
plt.legend()
plt.grid(True)
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig("People_Spending_Graph.png")
plt.show()
