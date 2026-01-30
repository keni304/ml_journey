# Day 2: Data Structures & Basic Stats

# 1. DATA: A dictionary representing daily study hours
study_data = {
    "Monday": 2,
    "Tuesday": 3,
    "Wednesday": 0, # Slacking off!
    "Thursday": 4,
    "Friday": 1,
    "Saturday": 5,
    "Sunday": 2
}

# 2. EXTRACT: Get just the numbers (values) from the dictionary
hours_list = list(study_data.values())

# 3. CALCULATE: Find the Average (Mean)
# Math: Total Sum / Number of Days
total_hours = sum(hours_list)
num_days = len(hours_list)
average_hours = total_hours / num_days

# 4. REPORT: Print the results
print("--- Study Analysis ---")
print(f"Total Hours: {total_hours}")
print(f"Average Hours per Day: {average_hours:.2f}")

# 5. LOGIC: Simple feedback
if average_hours > 3:
    print("Rating: Hardworking! 🚀")
elif average_hours > 1:
    print("Rating: Consistent. Keep it up. 👍")
else:
    print("Rating: You need to study more! ⚠️")