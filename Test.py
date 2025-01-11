
class Bank:
    def __init__(self, First_name, Second_name, Phone_number, Card_number, Address):
        self.First_name = First_name
        self.Second_name = Second_name
        self.Phone_number = Phone_number
        self.Card_number = Card_number
        self.Address = Address
        self.balance = 0.0
        
    # Account Creation      
    def Mydetails(self):
        print("The first Name is ", self.First_name)
        print("The second Name is ", self.Second_name)
        print("The phone Number is ", self.Phone_number)
        print("The card Number is ", self.Card_number)
        print("The Address is ", self.Address)
        print(f"Your Account created successful! \n {self.First_name} {self.Second_name} Welcome to NMB Bank!")
        print("\n")
        
# Input for account creation
First_name = input("Enter your First Name: ")
Second_name = input("Enter your Second name: ")
Phone_number = int(input("Enter your Phone Number: "))
Card_number = int(input("Enter your Card Number: "))
Address = input("Enter your Address: ")
print()

# Creating the object
b = Bank(First_name, Second_name, Phone_number, Card_number, Address)
# Calling the Method by using the object
b.Mydetails()

# Creating the subclass for deposit
class Deposit(Bank):
    def __init__(self, First_name, Second_name, Phone_number, Card_number, Address):
        super().__init__(First_name, Second_name, Phone_number, Card_number, Address)
        
    def Mydeposit(self, amount):
        self.amount = amount
        self.balance += amount
        print(f"{self.First_name} {self.Second_name}, Your Account has been credited with ${self.amount}. Current Balance: ${self.balance}\nThank you for Trusting our NMB Bank!" )

# Input for deposit
amount = float(input("Enter the amount you want to deposit: $"))

# Creating the object of Deposit class
deposit = Deposit(First_name, Second_name, Phone_number, Card_number, Address)
deposit.Mydeposit(amount)
print()

# Creating the subclass for withdrawal
class Withdrawal(Bank):
    def __init__(self, First_name, Second_name, Phone_number, Card_number, Address):
        super().__init__(First_name, Second_name, Phone_number, Card_number, Address)
        
    def Withdraw(self, amount):
        self.amount = amount
        
        if self.amount > self.balance:
            print("There is Insufficient amount in your Account!\nThank you for using NMB service!!")
        else:
            self.balance -= amount
            print(f"{self.First_name} {self.Second_name}, Your Account has been debited with ${self.amount}. Current Balance: ${self.balance}\nThank you for Trusting our NMB Bank!")

# Input for withdrawal
withdraw_amount = float(input("Enter the amount you want to withdraw: $"))

# Creating the object of Withdrawal class
withdraw = Withdrawal(First_name, Second_name, Phone_number, Card_number, Address)
withdraw.Withdraw(withdraw_amount)