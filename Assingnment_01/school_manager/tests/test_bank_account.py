# Name: Ahmad Ayaz
# Trainee ID: TRN-2026-000371
# Date: 09 November 2026

import pytest

class BankAccount:
    def __init__(self, balance: float = 0):
        self.balance = balance
        self.history: list[str] = []

    def deposit(self, amount: float) -> None:
        if amount <= 0:
            raise ValueError("Amount must be positive.")
        self.balance += amount
        self.history.append(f"deposit:{amount}")

    def withdraw(self, amount: float) -> None:
        if amount <= 0 or amount > self.balance:
            raise ValueError("Invalid withdrawal.")
        self.balance -= amount
        self.history.append(f"withdraw:{amount}")

@pytest.fixture
def account() -> BankAccount:
    return BankAccount(1000)

def test_deposit(account: BankAccount) -> None:
    account.deposit(250)
    assert account.balance == 1250

def test_withdraw(account: BankAccount) -> None:
    account.withdraw(300)
    assert account.balance == 700

def test_transaction_history(account: BankAccount) -> None:
    account.deposit(100)
    account.withdraw(50)
    assert account.history == ["deposit:100", "withdraw:50"]

def test_reject_zero_or_negative_deposit(account: BankAccount) -> None:
    with pytest.raises(ValueError):
        account.deposit(0)

def test_reject_overdraft(account: BankAccount) -> None:
    with pytest.raises(ValueError):
        account.withdraw(1001)
