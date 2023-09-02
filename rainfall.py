# Initialize an empty list to store daily rainfall data
rainfall_data = []

# Prompt the user to input rainfall data for each day of the week
for day in range(1, 8):
    while True:
        try:
            rainfall = float(input(f"Enter rainfall data for Day {day}: "))
            if rainfall >= 0:
                rainfall_data.append(rainfall)
                break
            else:
                print("Rainfall should be a non-negative number. Try again.")
        except ValueError:
            print("Invalid input. Please enter a number.")

# Find the day(s) with the minimum and maximum rainfall
min_rainfall = min(rainfall_data)
max_rainfall = max(rainfall_data)
min_days = [i + 1 for i, rainfall in enumerate(rainfall_data) if rainfall == min_rainfall]
max_days = [i + 1 for i, rainfall in enumerate(rainfall_data) if rainfall == max_rainfall]

# Display the results
print(f"\nMinimum rainfall ({min_rainfall} inches) occurred on:")
for day in min_days:
    print(f"Day {day}")

print(f"\nMaximum rainfall ({max_rainfall} inches) occurred on:")
for day in max_days:
    print(f"Day {day}")
