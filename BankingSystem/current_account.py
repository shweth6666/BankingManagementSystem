from bank_account import BankAccount

class CurrentAccount(BankAccount):
    """Current account with overdraft facility."""

    def __init__(self, account_no: str, balance: float = 0):
        super().__init__(account_no, balance)

    def withdraw(self, amount: float) -> bool:

        if amount <= self.balance + 5000:
            self._balance -= amount
            return True

        return False

    def calculate_interest(self) -> float:
        return 0

    def apply_service_charge(self) -> None:
        """Apply monthly service charge."""
        self._balance -= 100