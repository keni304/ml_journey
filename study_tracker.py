# Day 2: Interactive Data Tracker

print("--- 📊 Weekly Study Tracker 📊 ---")
print("Enter your study hours for each day:")

# 1. SETUP: List of days to ask about
days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
study_data = {} # Empty dictionary to store answers

# 2. INPUT LOOP: Ask the user for each day
for day in days:
    # Ask the question
    user_input = input(f"How many hours on {day}? ")
    
    # CONVERT: Text -> Decimal Number (Float)
    hours = float(user_input)
    
    # STORE: Put it in the dictionary
    study_data[day] = hours

# 3. CALCULATE
hours_list = list(study_data.values())
total_hours = sum(hours_list)
average_hours = total_hours / len(hours_list)

# 4. REPORT
print("\n--- 📈 Your Report ---")
print(f"Total Hours: {total_hours}")
print(f"Average: {average_hours:.2f} hours/day")

# 5. LOGIC
if average_hours >= 4:
    print("Rating: 🔥 ML Engineer Mode! (Excellent)")
elif average_hours >= 2:
    print("Rating: ✅ Consistent. (Good)")
else:
    print("Rating: ⚠️ You need to push harder!")