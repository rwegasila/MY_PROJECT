class Vehicle:
    def __init__(self, Colour_of_the_car, Age_of_the_car, Seat_of_the_car):
        self.Colour_of_the_car=Colour_of_the_car
        self.Age_of_the_car=Age_of_the_car
        self.Seat_of_the_car=Seat_of_the_car
        
        #Creating a metod of Vehicle class
    def Car_details(self):
        print("The car is of ", self.Colour_of_the_car)
        print("The age of the car is ", self.Age_of_the_car)
        print("Number of seats in the car are :", self.Seat_of_the_car)
        # Creating Objects for the Class
My_Car = Vehicle('Red', 5, 4)
Your_Car = Vehicle('Blue', 2, 6)
        # Accessing the Method using an Object
My_Car.Car_details()
print("\n")
Your_Car.Car_details()

class Car(Vehicle):
    def __init__(self, Model_Name, Speed_Limit):
        super().__init__('White','10', 22)   # Calling the parent constructor
        self.Model_Name=Model_Name
        self.Speed_Limit=Speed_Limit
        
        # Creating a method of Car class
    def Details(self):
        print("The model name of the car is ", self.Model_Name)
        print("The speed limit of the car is ", self.Speed_Limit," Km/Hr.")
        

#Creating the fuction for user input

My_first_model=input("Input the model of the car ")
My_second_model=input("The Speed of the car is ")
        
        

        
    