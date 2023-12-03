"""Employee pay calculator."""
"""ENTER YOUR SOLUTION HERE!"""

class Employee:
    def __init__(self, name, contract_type, salary=None, hourly_wage=None, hours_worked=None, bonus=None, contracts_landed=None, commission_per_contract=None):
        self.name = name
        self.contract_type = contract_type
        self.salary = salary
        self.hourly_wage = hourly_wage
        self.hours_worked = hours_worked
        self.bonus = bonus
        self.contracts_landed = contracts_landed
        self.commission_per_contract = commission_per_contract

    def get_pay(self):
        if self.contract_type == "salary":
            base_pay = self.salary
        else:
            base_pay = self.hourly_wage * self.hours_worked

        commission = 0
        if self.bonus is not None:
            commission += self.bonus
        if self.contracts_landed is not None:
            commission += self.contracts_landed * self.commission_per_contract

        return base_pay + commission

    def __str__(self):
        description = f"{self.name} works on a "
        if self.contract_type == "salary":
            description += f"monthly salary of {self.salary}"
        else:
            description += f"contract of {self.hours_worked} hours at {self.hourly_wage}/hour"

        if self.bonus is not None:
            description += f" and receives a bonus commission of {self.bonus}"
        elif self.contracts_landed is not None:
            description += f" and receives a commission for {self.contracts_landed} contract(s) at {self.commission_per_contract}/contract"

        total_pay = self.get_pay()
        description += f". Their total pay is {total_pay}."

        return description


billie = Employee('Billie', 'salary', salary=4000)
charlie = Employee('Charlie', 'hourly', hourly_wage=25, hours_worked=100)
renee = Employee('Renee', 'salary', salary=3000, contracts_landed=4, commission_per_contract=200)
jan = Employee('Jan', 'hourly', hourly_wage=25, hours_worked=150, contracts_landed=3, commission_per_contract=220)
robbie = Employee('Robbie', 'salary', salary=2000, bonus=1500)
ariel = Employee('Ariel', 'hourly', hourly_wage=30, hours_worked=120, bonus=600)


# Billie works on a monthly salary of 4000.  Their total pay is 4000.
billie = Employee('Billie')

# Charlie works on a contract of 100 hours at 25/hour.  Their total pay is 2500.
charlie = Employee('Charlie')

# Renee works on a monthly salary of 3000 and receives a commission for 4 contract(s) at 200/contract.  Their total pay is 3800.
renee = Employee('Renee')

# Jan works on a contract of 150 hours at 25/hour and receives a commission for 3 contract(s) at 220/contract.  Their total pay is 4410.
jan = Employee('Jan')

# Robbie works on a monthly salary of 2000 and receives a bonus commission of 1500.  Their total pay is 3500.
robbie = Employee('Robbie')

# Ariel works on a contract of 120 hours at 30/hour and receives a bonus commission of 600.  Their total pay is 4200.
ariel = Employee('Ariel')
