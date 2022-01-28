class Table:
    def __init__(self, no_of_diners):
        self.bill = []  # this bill list will store items, price and quantity/etc in a DICTIONARY
        self.diners = no_of_diners  # number of diners per table

    #  order method will accept item and a price
    #  method will append menu item to bill, if bill contains item with same item name and price, then it
    #   -should do quantity += quantity

    # Food 10.00 3
    def order(self, item, price, quantity=1):  # quantity by default is one unless changed
        # {"item": item, "price": price, "quantity": 6}
        for inputi in self.bill:  # inputi will go through the bill list
            # in the TEST CASE, BILL is EMPTY and so FOR LOOP IS SKIPPED as..
            # -a for loop WILL NOT go through an empty list
            if inputi['item'] == item and inputi['price'] == price:
                # VALUE of KEY in inputi COMPARED to VALUE of PARAMETER in def order()
                inputi['quantity'] += quantity  # VALUE OF KEY UPDATED with VALUE of PARAMETER
                return  # returns None
        # in test case ADDS DICTIONARY to list in self.bill, otherwise..
        # IF BILL HAS A DICTIONARY ALREADY, APPEND adds another dictionary
        self.bill.append({"item": item, "price": price, "quantity": quantity})

    # remove method will subtract quantity from item in bill with matching item and price
    def remove(self, item, price, quantity):
        for inputi in self.bill:  # Goes through bill # in test case bill is has order dictionary
        # in test case, self.bill has LIST of DICTIONARY already so parameter values compared with key values
            if inputi['item'] == item and inputi['price'] == price:
                # value of keys in bill -= with value of parameter
                inputi['quantity'] -= quantity
                if inputi['quantity'] == 0:  # if quantity = 0 then bill removed
                    self.bill.remove(inputi)
                return True
        return False

    # method that returns the total cost for the table based on the prices and quantities in the bill.
    def get_subtotal(self):
        # multiply price by quantity and then add to subtotal
        subtotal = 0
        for inputi in self.bill:  # goes through bill which already has THREE DICTIONARIES
            #  value of keys price and quantity (e.g. 10 * 3) RETURNED to subtotal
            subtotal += inputi["price"] * inputi["quantity"]
        return subtotal  # returns to actual variable in test case

    # method that accepts a service charge percentage in the form of a decimal.
    # If no service charge percentage is provided, it should default to 10% (i.e. 0.10)
    def get_total(self, service_charge_percentage=0.10):  # service charge by default is 0.10 if not provided
        subtotal = self.get_subtotal()  # use get_subtotal + has access to self.bill
        # this means that get_subtotal goes through the three orders again and value of subtotal is 50.60
        service_charge = subtotal * service_charge_percentage  # value of subtotal returned * 0.15 returned to subtotal
        total = subtotal + service_charge  # subtotal + service_charge returned to total
        return {"Sub Total": f"£{subtotal:.2f}", "Service Charge": f"£{service_charge:.2f}", "Total": f"£{total:.2f}"}
        # to 2 s.f. otherwise doesn't match test case
        # Example {"Sub Total": "£120.00", "Service Charge": "£12.00", "Total": "£132.00"}

    # A split_bill method, which returns the subtotal cost of the bill divided
    # -by the number of diners as a float rounded up to the nearest penny.
    def split_bill(self):
        subtotal = self.get_subtotal()  # value of subtotal is 53.2
        total = subtotal / self.diners  # number of diners (6) divided by subtotal (53.2)
        return total
