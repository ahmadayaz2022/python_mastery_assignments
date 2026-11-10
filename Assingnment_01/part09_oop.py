# Name: Ahmad Ayaz
# Trainee ID: TRN-2026-000371
# Date: 09 November 2026

# Warm-up: Student class
class Student:
    def __init__(self, name: str, roll_number: int, marks: list[float]):
        self.name = name
        self.roll_number = roll_number
        self.marks = marks

    def average(self) -> float:
        return sum(self.marks) / len(self.marks) if self.marks else 0.0

    def add_mark(self, mark: float) -> None:
        if not 0 <= mark <= 100:
            raise ValueError("Mark must be between 0 and 100.")
        self.marks.append(mark)

    def __str__(self) -> str:
        return f"{self.name} (Roll {self.roll_number}): avg {self.average():.1f}"

student = Student("Ali", 12, [80, 82, 81])
student.add_mark(81)
print(student)

# Build: Bank account
class BankAccount:
    def __init__(self, owner: str, balance: float = 0.0):
        if balance < 0:
            raise ValueError("Opening balance cannot be negative.")
        self.owner = owner
        self.balance = balance
        self.history: list[str] = [f"Opening balance: Rs {balance:.2f}"]

    def deposit(self, amount: float) -> None:
        if amount <= 0:
            raise ValueError("Deposit must be greater than zero.")
        self.balance += amount
        self.history.append(f"Deposited Rs {amount:.2f}")

    def withdraw(self, amount: float) -> None:
        if amount <= 0:
            raise ValueError("Withdrawal must be greater than zero.")
        if amount > self.balance:
            raise ValueError("Insufficient balance.")
        self.balance -= amount
        self.history.append(f"Withdrew Rs {amount:.2f}")

account = BankAccount("Ahmad", 1000)
account.deposit(500)
account.withdraw(200)
print("Balance:", account.balance)
print("Transactions:", account.history)

# Challenge: Library composition and EBook inheritance
class Book:
    def __init__(self, title: str, author: str, available: bool = True):
        self.title = title
        self.author = author
        self.available = available

    def __str__(self) -> str:
        return f"{self.title} by {self.author} ({'Available' if self.available else 'Borrowed'})"

class EBook(Book):
    def __init__(self, title: str, author: str, file_size_mb: float, available: bool = True):
        super().__init__(title, author, available)
        self.file_size_mb = file_size_mb

    def __str__(self) -> str:
        return f"E-book: {self.title} by {self.author} - {self.file_size_mb:.1f} MB"

class Library:
    def __init__(self):
        self.books: list[Book] = []

    def add_book(self, book: Book) -> None:
        self.books.append(book)

    def borrow(self, title: str) -> bool:
        for book in self.books:
            if book.title.lower() == title.lower() and book.available:
                book.available = False
                return True
        return False

    def return_book(self, title: str) -> bool:
        for book in self.books:
            if book.title.lower() == title.lower() and not book.available:
                book.available = True
                return True
        return False

    def available_books(self) -> list[Book]:
        return [book for book in self.books if book.available]

library = Library()
library.add_book(Book("Python Basics", "A. Khan"))
library.add_book(EBook("Learning AI", "S. Ali", 4.5))
print("Borrow successful:", library.borrow("Python Basics"))
print("Available books:", [str(book) for book in library.available_books()])
print("Return successful:", library.return_book("Python Basics"))
