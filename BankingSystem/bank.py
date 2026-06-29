class Bank:

    def __init__(self):
        self.customers = []

    def add_customer(self, customer):
        self.customers.append(customer)

    def find_customer(self, customer_id):

        for customer in self.customers:
            if customer.customer_id == customer_id:
                return customer

        return None