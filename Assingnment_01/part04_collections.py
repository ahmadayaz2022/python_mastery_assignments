# Name: Ahmad Ayaz
# Trainee ID: TRN-2026-000371
# Date: 09 November 2026

# Shopping list
print("Welcome to the shopping list manager!")

items = ["milk", "bread", "eggs"]
items.append("tea")
items.remove("bread")
items.sort()
print("Shopping list:")
for index, item in enumerate(items, start=1):
    print(f"{index}. {item}")

# Phone book
contacts = {
    "Ali": "03001234567",
    "Sara": "03111234567",
    "Usman": "03221234567",
    "Ayesha": "03331234567",
    "Hamza": "03441234567",
}

while True:
    print("\n1) Add  2) Search  3) Delete  4) Show all  5) Exit")
    choice = input("Choose: ").strip()
    if choice == "1":
        print("Add a new contact")
        name = input("Contact name: ").strip()
        phone = input("Phone number: ").strip()
        contacts[name] = phone
        print("Contact saved.")
    elif choice == "2":
        print("Search for a contact")
        name = input("Name to search: ").strip()
        phone = contacts.get(name)
        print(f"{name}: {phone}" if phone else "Not found")
    elif choice == "3":
        print("Delete a contact")
        name = input("Name to delete: ").strip()
        if name in contacts:
            del contacts[name]
            print("Contact deleted.")
        else:
            print("Not found")
    elif choice == "4":
        print("Show all contacts")
        if contacts:
            for name, phone in sorted(contacts.items()):
                print(f"{name}: {phone}")
        else:
            print("Phone book is empty.")
    elif choice == "5":
        break
    else:
        print("Invalid menu choice.")

# Class result sheet
results = {
    "Ali": [80, 72, 91],
    "Sara": [95, 88, 90],
    "Usman": [35, 68, 74],
    "Ayesha": [82, 39, 91],
    "Hamza": [65, 70, 78],
}
topper_name = ""
topper_average = -1
students_below_40 = set()

for student, marks in results.items():
    total = sum(marks)
    average = total / len(marks)
    print(f"{student}: total={total}, average={average:.2f}")
    if average > topper_average:
        topper_name, topper_average = student, average
    if any(mark < 40 for mark in marks):
        students_below_40.add(student)

print(f"Class topper: {topper_name} ({topper_average:.2f})")
print("Below 40 in at least one subject:", students_below_40)
