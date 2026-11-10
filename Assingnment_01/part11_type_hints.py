# Name: Ahmad Ayaz
# Trainee ID: TRN-2026-000371
# Date: 09 November 2026

from dataclasses import asdict, dataclass, field
import json
from pathlib import Path

@dataclass(order=True)
class Product:
    # Sorting compares fields in declaration order; price is first for price sorting.
    price: float
    name: str
    stock: int
    tags: list[str] = field(default_factory=list)

    def __post_init__(self) -> None:
        if self.price < 0:
            raise ValueError("Price cannot be negative.")
        if self.stock < 0:
            raise ValueError("Stock cannot be negative.")

products = [
    Product(1200.0, "Keyboard", 5, ["computer", "accessory"]),
    Product(800.0, "Mouse", 0, ["computer", "accessory"]),
    Product(2500.0, "Headphones", 0, ["audio"]),
    Product(500.0, "Notebook", 12, ["stationery"]),
    Product(3500.0, "Monitor", 3, ["computer"]),
]

print("Out-of-stock products:")
for product in products:
    if product.stock == 0:
        print(product)

# Save and load JSON
json_path = Path("products.json")
json_path.write_text(json.dumps([asdict(product) for product in products], indent=4), encoding="utf-8")
loaded_data = json.loads(json_path.read_text(encoding="utf-8"))
loaded_products = [Product(**item) for item in loaded_data]
loaded_products.sort()  # price is the first dataclass field
print("Products sorted by price:")
for product in loaded_products:
    print(product)
