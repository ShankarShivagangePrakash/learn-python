class ATM:
    """
        For encapsulation, we have to bind data and methods together
        we achieve it using class
        But we shouldn't allow direct access to data members outside the class.
        To achieve this, we have to make data members private
            To make any member variable private do __<variableName>
            If you notice balance has been made private using __balance
            while accessing this data member anywhere inside the class you have to use __<variableName>
    """
    def __init__(self, balance=0):
        self.__balance = balance

    # accessing private member balance using __ as __balance.
    def deposit(self, amount):
        self.__balance += amount

    def withdraw(self, amount):
        self.__balance -= amount

    def balance(self):
        print(self.__balance)

account1 = ATM()
account1.deposit(100)
account1.withdraw(50)
account1.balance()

account2 = ATM(1000)
account2.deposit(100)
account2.withdraw(500)
account2.balance()
