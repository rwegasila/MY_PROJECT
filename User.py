class User:
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender
        
    def show_user_details(self):
         print("Name:", self.name)
         print("Age:", self.age)
         print("Gender:", self.gender)
         
name = input("Enter your name: ")
age = input("Enter your age: ")
gender = input("Enter your gender: ")

#P = User(name, age, gender)
#P.show_user_details()

class Bank(User):
    def __init__(self, name, age, gender):
        super().__init__(name, age, gender)
        self.balance = 0
        
    def deposit(self, amount):
        self.amount = amount
        self.balance += self.amount
        print("Account balance has been updated: $", self.balance)
        
    def withdraw(self, amount):
        self.amount = amount
        if self.amount > self.balance:
            print("Insufficient Fund | Balance available: $", self.balance)
        else:
            self.balance -= self.amount
            print("Account balance has been updated: $", self.balance)
            
    def view_details(self):
        self.show_user_details()
        print("Account balance is: $", self.balance)

# Example usage:
amount = float(input("Enter the amount: "))
bank_user = Bank(name, age, gender)
bank_user.deposit(amount)
bank_user.withdraw(500)  # Example withdrawal
bank_user.view_details()