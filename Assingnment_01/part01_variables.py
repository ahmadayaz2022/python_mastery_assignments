# Name: Ahmad Ayaz
# Trainee ID: TRN-2026-000371
# Date: 09 November 2026

# Warm-up: Student ID card

print("Student ID card")
name = input("Enter your name: ").strip()
age = int(input("Enter your age: "))
student_class = input("Enter your class: ").strip()
city = input("Enter your city: ").strip()

print("\n======== STUDENT CARD ========")
print(f"Name : {name}")
print(f"Age  : {age}")
print(f"Class: {student_class}")
print(f"City : {city}")
print("==============================")
print("Data types:")
print("name:", type(name).__name__)
print("age:", type(age).__name__)
print("class:", type(student_class).__name__)
print("city:", type(city).__name__)

# Build: Shop bill
print('Shop bill')
item_name = input("\nEnter item name: ").strip()
price = float(input("Enter price per item (Rs): "))
quantity = int(input("Enter quantity: "))

subtotal = price * quantity
discount = subtotal * 0.05
discounted_amount = subtotal - discount
tax = discounted_amount * 0.17
total = discounted_amount + tax

print("\n========== SHOP BILL ==========")
print(f"Item: {item_name}")
print(f"Quantity: {quantity}")
print(f"Subtotal: Rs {subtotal:.2f}")
print(f"Discount (5%): Rs {discount:.2f}")
print(f"Tax (17%): Rs {tax:.2f}")
print(f"Final total: Rs {total:.2f}")
