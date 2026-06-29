from abc import ABC, abstractmethod

class BankAccount(ABC):
    """Abstract base class for all bank accounts."""

    def __init__(self, account_no: str, balance: float = 0):
        self._account_no = account_no
        self._balance = balance

    @property
    def balance(self) -> float:
        """Returns current account balance."""
        return self._balance

    def deposit(self, amount: float) -> None:
        """Deposits money into the account."""
        self._balance += amount

    @abstractmethod
    def withdraw(self, amount: float) -> bool:
        """Withdraw money from account."""
        pass

    @abstractmethod
    def calculate_interest(self) -> float:
        """Calculate account interest."""
        pass