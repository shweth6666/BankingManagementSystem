from bank_account import BankAccount

class SavingsAccount(BankAccount):
    """Savings account with minimum balance rule."""

    def __init__(self, account_no: str, balance: float = 0):
        super().__init__(account_no, balance)

    def withdraw(self, amount: float) -> bool:

        if self.balance - amount >= 500:
            self._balance -= amount
            return True

        return False

    def calculate_interest(self) -> float:
        return self.balance * 0.04