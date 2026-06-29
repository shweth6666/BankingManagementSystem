from abc import ABC, abstractmethod

class BankAccount(ABC):

    def __init__(self, account_no, balance=0):
        self._account_no = account_no
        self._balance = balance

    @property
    def balance(self):
        return self._balance

    def deposit(self, amount):
        self._balance += amount

    @abstractmethod
    def withdraw(self, amount):
        pass

    @abstractmethod
    def calculate_interest(self):
        pass