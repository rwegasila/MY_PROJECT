class Banksystem:
    def __init__(self, First_name, Last_name, Age, Gender, Address, Card_number):
         self.First_name=First_name
         self.Last_name=Last_name
         self.Age=Age
         self.Gender=Gender
         self.Address=Address
         self.Card_number=Card_number


#Creating the method
    def mydetails(self):
         print("The First Name is  ", self.First_name)
         print("The Last Name is  ", self.Last_name)
         print("The Age is  ", self.Age)
         print("The gender is ", self.Gender)
         print("The Address is ", self.Address)
         print("The Card Number is ", self.Card_number)
         print(self.First_name, self.Last_name, "Your Account Is created Succesfully! Welcome to NMB Bank!")
         print("\n")
         
    

#For user input
First_name=input("Enter Your First Name: ")
Last_name=input("Enter Your Last Name: ")
Age=int(input("Enter Your Age: "))
Gender=input("Enter Your Gender: ")
Address=input("Enter Your Address: ")
Card_number=int(input("Enter Your Card Number: "))
print("\n")
print(".................................................................................")
#Creating the object
P=Banksystem(First_name, Last_name, Age, Gender, Address, Card_number)
P.mydetails()

#Crating a Chird Class For User to deposite Money

class deposite(Banksystem):
     def __init__(self, First_name, Last_name, Age, Gender, Address, Card_number):
          super().__init__(First_name, Last_name, Age, Gender, Address, Card_number)
          self.balance=0


#Creating the Method of the chird class for deposite

     def Money(self, amount):
          self.amount=amount
          self.balance=self.balance+amount
          print("Your Account is Activated to  ", self.balance)


#Creating the Method for User to withdraw Money

     def withdrawer(self, withdraw):
          self.withdraw=withdraw
          if withdraw>amount:
               print("Sorry !", self.First_name, self.Last_name, "Your having insuficient amount in your Account!", self.balance)

          else:
               self.balance=self.balance-withdraw
               print("The remaining amount after withdraw is  ", self.balance) 

#For user input
amount=int(input("Enter the Amount You What to deposite "))
withdraw=int(input("Enter the amount you what to withdraw !"))

#creating the object for user to deposite
B=deposite(First_name, Last_name, Age, Gender, Address, Card_number)

#for Information Display
B.Money(amount)
B.withdrawer(withdraw)