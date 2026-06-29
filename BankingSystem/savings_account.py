from bank_account import BankAccount

class SavingsAccount(BankAccount):

    def withdraw(self, amount):
        if self.balance - amount >= 500:
            self._balance -= amount
            return True
        return False

    def calculate_interest(self):
        return self.balance * 0.04