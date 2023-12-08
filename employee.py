"""Employee pay calculator."""
"""ENTER YOUR SOLUTION HERE!"""


class Employee:
    def __init__(self, name, contract_type="salary", salary=0, hourly_wage=0, hours_worked=0, bonus=0, contracts_landed=0, commission_per_contract=0):
        self.name = name
        self.contract_type = contract_type
        self.salary = salary
        self.hourly_wage = hourly_wage
        self.hours_worked = hours_worked
        self.bonus = bonus
        self.contracts_landed = contracts_landed
        self.commission_per_contract = commission_per_contract

    def get_pay(self):
        
        base_pay = self.salary if self.contract_type == "salary" else self.hourly_wage * self.hours_worked

       
        commission = self.bonus + (self.contracts_landed * self.commission_per_contract)

        return base_pay + commission

    def __str__(self):
        
        description = f"{self.name} works on a "
        if self.contract_type == "salary":
            description += f"monthly salary of {self.salary}"
        else:
            description += f"contract of {self.hours_worked} hours at {self.hourly_wage}/hour"

       
        if self.bonus > 0:
            description += f" and receives a bonus commission of {self.bonus}"
        if self.contracts_landed > 0:
            description += f" and receives a commission for {self.contracts_landed} contract(s) at {self.commission_per_contract}/contract"

    
        total_pay = self.get_pay()
        description += f". Their total pay is {total_pay}."

        return description

# Employee objects
billie = Employee('Billie', 'salary', salary=4000)
charlie = Employee('Charlie', 'hourly', hourly_wage=25, hours_worked=100)
renee = Employee('Renee', 'salary', salary=3000, contracts_landed=4, commission_per_contract=200)
jan = Employee('Jan', 'hourly', hourly_wage=25, hours_worked=150, contracts_landed=3, commission_per_contract=220)
robbie = Employee('Robbie', 'salary', salary=2000, bonus=1500)
ariel = Employee('Ariel', 'hourly', hourly_wage=30, hours_worked=120, bonus=600)



