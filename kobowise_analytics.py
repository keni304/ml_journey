import pandas as pd

# Transaction data for KoboWise
data = {
    "Date": ["2025-01-01", "2025-01-02", "2025-01-03", "2025-01-04", "2025-01-05"],
    "Category": ["Food", "Transport", "Data", "Food", "Books"],
    "Amount": [5000, 1500, 3000, 4500, 12000],
    "Description": ["Jollof Rice", "Uber to UI", "MTN Sub", "Amala", "Python Textbook"]
}

# Convert dictionary to DataFrame
df = pd.DataFrame(data)

# Display all transactions
print("\n--- KoboWise Transaction Log ---")
print(df)

# Calculate summary metrics
total_spent = df["Amount"].sum()
average_spend = df["Amount"].mean()

print("\n--- Financial Summary ---")
print(f"Total Spent: N{total_spent:,.2f}")
print(f"Average Transaction: N{average_spend:,.2f}")

# Filter for Food category
print("\n--- Food Expenses ---")
food_expenses = df[df["Category"] == "Food"]
print(food_expenses)

# Export data to CSV
df.to_csv("kobowise_data.csv", index=False)
print("\nExport complete. Data saved to 'kobowise_data.csv'.")