# FOLLOWING THE SPARTA GLOBAL LEARNING PATHWAY THE FOLLOWING CODE WAS CREATED
# code not my own but from my own compiler


############### MAIN ################

import customer
import employee
import random

# randomly give customer or employee POLYMORPHISM
if random.randint(0, 1) == 0:
    # encapsulation & inheritance

    my_person = customer.Customer('first name 1', 
                                  'last name 2', 
                                  'address ')
    # my_person.first_name = 'uh'
else:
    # inheritance & polymorphism

    my_person = employee.Employee('Utmost', 
                                  'Appreciation', 
                                  'Marketing ')
my_person.print()

############## Customer.py ##########


import person


class Customer(person.Person):
    def __init__(self, fname, lname, address):
        self._address = address
        super().__init__(fname, lname)

    def print(self):
        print(f'Address: {self._address}', end='')
        super().print()


############## Person.py ############


class Person:
    def __init__(self, fname, lname):
        self._first_name = fname
        self._last_name = lname

    def print(self):
        print(f'Full name: {self._first_name} {self._last_name}')

    @property
    def first_name(self):
        print('In get method')
        return self._first_name

    @first_name.setter
    def first_name(self, new_first_name):
        print('in set method')
        self._first_name = new_first_name


############## Employee.py ############


import person


class Employee(person.Person):
    def __init__(self, fname, lname, department):
        self._department = department
        super().__init__(fname, lname)

    def print(self):
        print(f'Department: {self._department}', end='')
        super().print()


########################################

