import math

class Table:
    def __init__(self, diners):
        # What to include is specified in README
        self.diners = diners # Required for split bill function
        self.bill = [] # Because we have to refer to the bill in each method, specify here

    # If quantity is not input then it is automatically set to 1
    def order(self, item, price, quantity= 1):
        for entry in self.bill:
            # Check if same item is already listed
            if entry["item"] == item: # and entry["price"] == price:
                # If item is the same and OPTIONALLY price is the same
                entry["quantity"] += quantity
                # This isn't used in the main example here, but if the item was found, it would update
                return
        # If the item isn't already included then it must be appended
        self.bill.append({"item": item, "price": price, "quantity": quantity})


    # In this section it was difficult to keep track of what leads to True Vs False
    def remove(self, item, price, quantity):
        # This is a requirement of our test criteria even if omitting is not detected by the test module
        if quantity <= 0:
            return False

        for entry in self.bill:

            # Price must be included since it is a requirement of the test module
            if entry["item"] == item and entry["price"] == price:
                if entry["quantity"] >= quantity:
                    # Case 1
                    entry["quantity"] -= quantity
                    if entry["quantity"] == 0:
                        # Case 2
                        self.bill.remove(entry)
                    return True
                else:
                    return False
        return False

    def get_subtotal(self):
        # Must loop through the bill since entries have been appended
        subtotal = sum(entry["price"] * entry["quantity"] for entry in self.bill)
        return round(subtotal, 2)

    def get_total(self, service_charge_percentage=0.10):
        subtotal = self.get_subtotal()
        service_charge = round(subtotal * service_charge_percentage, 2)
        total = subtotal + service_charge
        return {
            "Sub Total": f"£{subtotal:.2f}",
            "Service Charge": f"£{service_charge:.2f}",
            "Total": f"£{total:.2f}",
        }

    def split_bill(self):
        subtotal = self.get_subtotal()
        # The ceiling function allows us to round up, the * 100 / 100 is necessary for this operation
        per_diner_cost = math.ceil(subtotal / self.diners * 100) / 100

        return per_diner_cost
        # NOTE: { "Total per diner" : f"{per_diner_cost:.2f}"} does not work Ah look at module...
        # NOTE:    f"The cost per diner is {per_diner_cost}" is not allowed as it is not a dictionary
