# Name: Ahmad Ayaz
# Trainee ID: TRN-2026-000371
# Date: 09 November 2026

import copy

# Warm-up: Predict, then run
# Prediction: b refers to the same list as a, so appending through b changes a.
a = [1, 2, 3]
b = a
b.append(4)
print("a after changing b:", a)

# Prediction: c is a separate shallow copy, so appending to c does not change a.
c = a.copy()
c.append(5)
print("a and c:", a, c)

# Prediction: a is b is True; a is c is False; a == a[:] is True (equal values).
print(a is b, a is c, a == a[:])

# Build: Fix the shared-cart default argument bug
def add_item_bad(item: str, cart: list[str] = []) -> list[str]:
    cart.append(item)
    return cart

print("Bug demonstration:")
print(add_item_bad("Book"))
print(add_item_bad("Pen"))  # Pen is added to the same old list.

def add_item(item: str, cart: list[str] | None = None) -> list[str]:
    if cart is None:
        cart = []
    cart.append(item)
    return cart

print("Fixed function:")
print(add_item("Book"))
print(add_item("Pen"))

# Challenge: Shallow copy vs deep copy
classes = {"A": ["Ali", "Sara"]}
shallow = classes.copy()
deep = copy.deepcopy(classes)

shallow["A"].append("Usman")
print("After editing shallow copy:")
print("original:", classes)
print("shallow:", shallow)
print("deep:", deep)

deep["A"].append("Ayesha")
print("After editing deep copy:")
print("original:", classes)
print("deep:", deep)
