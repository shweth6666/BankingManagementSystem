class Customer:
    """Represents a bank customer."""

    def __init__(self, customer_id: str, name: str):
        self.customer_id = customer_id
        self.name = name
        self.account = None
        self.transactions = []