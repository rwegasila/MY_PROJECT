class Userr:
    def __init__(self, name, age , gender):
        self.name=name
        self.age=age
        self.gender=gender
        
    def Mydetails(self):
        print("Name: ", self.name)
        print("Age: ", self.age)
        print("Gender: ", self.gender)
        
name=input("Enter your name ")
age=input("Enter your age ")
gender=input("Enter your gender ")


#Creating a child class

class Bank(Userr):
    def __init__(self, name, age, gender):
        super().__init__(name, age, gender)
        self.balance=0
        
    def deposite(self, amount):
        self.amount=amount
        self.balance=self.balance+self.amount
        print("Account balance has been updated $", self.balance)
        
    def withdraw(self, amount):
        self.amount=amount
        if self.amount>self.balance:
            print("Insufficient Fund l Balance availabe $", self.balance)
             
        else:
            self.balance=self.balance-self.amount
            print("Accopunt has been updated $ ", self.balance)
            
    def view_details(self):
        print("Account balance: $", self.balance )
        
amount=float(input("Enter the amount"))
bank_user=Bank(name, age, gender)
bank_user.deposite(amount)
bank_user.withdraw(1000) #Example of withdrwal
bank_user.Mydetails()