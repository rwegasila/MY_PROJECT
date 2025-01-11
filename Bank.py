class Bank:
    def __init__(self, First_name, Second_name, Phone_number, Card_number, Addresss):
        self.First_name=First_name
        self.Second_name=Second_name
        self.Phone_number=Phone_number
        self.Card_number=Card_number
        self.Address=Addresss
        
  #Account Creation      
    def Mydetails(self):
        print("The first Name is.... ", self.First_name)
        print("The second Name is.... ", self.Second_name)
        print("The phone Number is.... ", self.Phone_number)
        print("The card Number is.... ", self.Card_number)
        print("The Address is.... ", self.Address)
        print(f"Your Account created successful! \n {self.First_name} {self.Second_name} Welocome to NMB Bank!")
        print("\n")
        
        
        
First_name=input("Enter your First Name ")
Second_name=input("Enter your Second name ")
Phone_number=int(input("Enter your Phone Number "))
Card_number=int(input("Enter your Card Number "))
Address=input("Enter your Address ")
print("\n")
#Creating the object
b=Bank(First_name, Second_name, Phone_number, Card_number,Address)
#Calling the Method by using the object
b.Mydetails()
         
 #Creating the subclass for deposit
class Deposit(Bank):
    def __init__(self, First_name, Second_name, Phone_number, Card_number, Addresss):
        super().__init__(First_name, Second_name, Phone_number, Card_number, Addresss)
        self.balance=0.0
        
    def Mydeposit(self, amount):
        self.amount=amount
        self.balance=self.balance+amount
        print(f"{self.First_name}  {self.Second_name} Your Account has been activated.... $ {self.balance} \n Thank you for Trusting our NMB Bank!\n" )
        
   #Creating the method for Withdraw
    def Withdraw(self, withdraw):
        self.withdraw=withdraw
        if self.withdraw>self.balance:
            print(f"There is insufficient amount in your Account.... $ {self.balance} \n Thank you for using NMB cervices!!\n")
        else:
            self.balance =self.balance-withdraw
            print("The remaining amount in your account after Withdraw is.... $ ", self.balance)
            
            #Creating the method for Fund Transfer
    def Transfer(self, transfer):
        self.transfer=transfer
        if self.transfer>self.balance:
            print(f"There is inssuficient Amount in your Account! ${self.balance} \n Thank you for using NMB Bank cervices!! ")
        else:
            self.balance=self.balance-transfer
            print(f"The amount $ {transfer} was transferea sucssesfully! \n The remaining Amount after transfer is.... $ {self.balance}\n Thank you for using NMB cervices!")

   #Creating the method for Bill payment by using ATM Bank
    def Bill_Payment(self, Bills):
        self.Bills=Bills
        self.balance=self.balance-Bills
        if self.balance>self.Bills:
              print('Select any aption to pay your Bill!!')
            
              print("1.Water Bill Payment\n 2.Electricity Bill Payment\n 3.School Fees Payment\n 4.Online Shoping Payment")
        option=input('')
            
        if option==1:
               print(f"The amount ${Bills} for water Bill was payed sucssesfully!!\n Thank you for using NMB services!!")
            
        if option==2:
                print(f"The amount ${Bills} for Electricity Bill was payed sucssesfully!!\n Thank you for using NMB services!!")
                
        if option==3:
                 print(f"The amount ${Bills} for School fees was payed sucssesfully!!\n Thank you for using NMB services!!")
         
        if option==4:
                  print(f"The amount ${Bills} Online Shoping Payment was payed sucssesfully!!\n Thank you for using NMB services!!")
        else:
                  print("There is Insufficient amount in your account!!\nThank you for using NMB Bank!")
            
                 
#Creating the object of Deposit class
deposit=Deposit(First_name, Second_name, Phone_number, Card_number,Address)
amount=float(input("Enter the amount you what to deposit\n $"))
withdraw=float(input("Enter the amount you what to withdraw \n$"))
transfer=float(input("Enter the amount you want to transfer\n $"))
Bills=float(input("Enter the amount you want to pay $"))

#Calling the method
deposit.Mydeposit(amount)
deposit.Withdraw(withdraw)
deposit.Transfer(transfer)
deposit.Bill_Payment(Bills) 

              
               


        
        

            






    
