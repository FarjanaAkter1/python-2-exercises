
#ex 6
class TaxMan:
    def __init__(self, items, tax_percentage):
        self.items = items

        # Convert the tax percentage from a string to a decimal value
        # by removing the percentage symbol and dividing by 100
        self.tax_percentage = float(tax_percentage.strip("%")) / 100

        self.total = None

    def calc_total(self):
        # Calculate the total price of all items using a generator expression
        total_price = sum(item["price"] for item in self.items)

        # Calculate the tax amount by multiplying the total price by the tax percentage
        tax_amount = total_price * self.tax_percentage

        # Round the total amount (including tax) to two decimal places
        self.total = round(total_price + tax_amount, 2)
        
    def get_total(self):
        # Return the total amount (including tax)
        return self.total
