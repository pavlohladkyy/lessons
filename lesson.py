# Завдання на інкапсуляцію

# 1. Створи клас BankAccount з приватними атрибутами balance та owner.
#    Додай метод deposit(amount) для внесення грошей і метод withdraw(amount) для зняття.
#    Реалізуй перевірку, щоб користувач не міг зняти більше, ніж є на рахунку.

class BankAccount:
    def __init__(self,balance,owner):
        self.balance = balance
        self.__owner = owner

    def deposit(self,amount):
        print(f"{self.__owner} your balance before deposite  {self.balance} ")
        self.balance += amount
        print(f"{self.__owner} your balance after deposite {self.balance} ")

    def _withdraw(self,amount):
        if not amount > self.balance:
            print(f"{self.__owner} your balance before withdraw  {self.balance} ")
            self.balance -= amount
            print(f"{self.__owner} your balance after withdraw {self.balance} ")
        else:
            print(f"User {self.__owner} you can't get more cash than you have on your balance")

balance = int(input("Введіть суму яка буде на балансі:")) #12
name = input("Введіть своє ім'я:")
bank = BankAccount(balance,name)
print(bank.deposit(12)) #24
print(bank.balance)
print(bank.withdraw(6)) #18
# хахаахахахахаха
