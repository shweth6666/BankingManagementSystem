from bank_account import BankAccount

class CurrentAccount(BankAccount):

    def withdraw(self, amount):

        if amount <= self.balance + 5000:
            self._balance -= amount
            return True

        return False

    def calculate_interest(self):
        return 0

    def apply_service_charge(self):
        self._balance -= 100