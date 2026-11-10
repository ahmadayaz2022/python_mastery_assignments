# Name: Ahmad Ayaz
# Trainee ID: TRN-2026-000371
# Date: 09 November 2026

# Warm-up: Even, odd and sign
try:
    number = int(input("Enter an integer: "))
    if number > 0:
        print("Positive")
    elif number < 0:
        print("Negative")
    else:
        print("Zero")
    print("Even" if number % 2 == 0 else "Odd")
except ValueError:
    print("Please enter a valid integer.")

# Build: Grade calculator
try:
    marks = float(input("\nEnter marks out of 100: "))
    if not 0 <= marks <= 100:
        print("Invalid marks")
    elif marks >= 80:
        print("Grade: A")
    elif marks >= 70:
        print("Grade: B")
    elif marks >= 60:
        print("Grade: C")
    elif marks >= 33:
        print("Grade: D")
    else:
        print("Grade: Fail")
except ValueError:
    print("Please enter a numeric mark.")

# Challenge: Electricity bill (progressive slabs)
try:
    units = float(input("\nElectricity units used: "))
    if units < 0:
        print("Units cannot be negative.")
    else:
        if units <= 100:
            energy_cost = units * 10
        elif units <= 200:
            energy_cost = 100 * 10 + (units - 100) * 15
        else:
            energy_cost = 100 * 10 + 100 * 15 + (units - 200) * 20
        print(f"Total electricity bill: Rs {energy_cost + 50:.2f}")
except ValueError:
    print("Please enter a valid number of units.")
