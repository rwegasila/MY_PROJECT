class User:
    def __init__(self, name, age, gender):
        self.name=name
        self.age=age
        self.gender=gender

#Creating a method of parent class

    def show_details(self):
     print("Personal details ")
     print("My name is ", self.name)
     print("I m ", self.age ,"Years old")
     print("gender", self.gender)


#geting the user input
name=input('Enter your name')
age=int(input('Enter your Age'))
gender=input('Enter your gender')


#Creating a Child Class

class BankUser(User):
   def __init__(self, name, age, gender):
      super().__init__(name, age, gender)
      self.balance=0


#Creating the method to deposit amount

   def deposite(self, amount):
      if (amount>0):
       self.balance=self.balance+amount
       print(f"Deposite Successful! Your new balance is {self.balance}" )

#Creating the object 
X= BankUser(name, age, gender)


X.show_details()
if (age>40):
   print('Im not a student')
else:
   print('Im a student')


#Printing the result

dep_amount=float(input('Enter the amount you want to deposite'))
X.deposite(dep_amount)