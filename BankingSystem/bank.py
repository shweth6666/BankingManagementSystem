class Bank:
    """Manages customers and banking operations."""

    def __init__(self):
        self.customers = []

    def add_customer(self, customer) -> None:
        self.customers.append(customer)

    def find_customer(self, customer_id: str):

        for customer in self.customers:
            if customer.customer_id == customer_id:
                return customer

        return None