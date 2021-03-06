from typing import Type
from IPython.display import clear_output
from traitlets.traitlets import Instance

class Parking_Garage():
    def __init__(self):
        self.tickets = list(range(1,201))
        self.parkingSpaces = list(range(1,201))
        self.currentTicket = {}


    def takeTicket(self):
        input('Press enter to print ticket')
        clear_output()
        if len(self.parkingSpaces) > 0:
            for i in self.parkingSpaces:
                self.tickets.remove(self.tickets[0])
                space = self.parkingSpaces[0]
                self.parkingSpaces.remove(space)
                self.currentTicket[space] = 10 
                break
            return space
        else:
            print("Parking Garage is Full.")
            clear_output()
        


    def payForParking(self):
        space = int(input('Please enter your parking space number: '))
        clear_output()
        if space not in self.currentTicket:
            print('Sorry that is not a valid number. Please Enter a valid number.')   
            self.payForParking()
        else:
            space = int(space) 
        payment= self.Payment(space)
        if payment != 0:
            owe = "Your total is now $" + str(payment)
            return owe
        else:
            print("Thank you, your payment has been processed.\nYou have 15 minutes to exit the parking garage.")
            clear_output()
            return space
        
    def Payment(self, space):
        print('Your total is $' + str(self.currentTicket[space]))
        amount = input('Please enter amount you are paying: ')
        if amount.isdigit() and int(amount) < self.currentTicket[space]:
            self.currentTicket[space] -= int(amount)
            self.currentTicket[space]= self.currentTicket[space]
            return self.currentTicket[space]
        elif amount.isdigit() == False or int(amount) > self.currentTicket[space]:
            print('Sorry that is not a valid number. Please Enter a valid number.')
            self.Payment(space)
        else:
            self.currentTicket[space] = True
            return 0

        
    def LeaveGarage(self):
        space = input('Please enter your parking space number: ')
        clear_output()
        space= int(space)
        if self.currentTicket[space] == True:
            farewell= "Thanks for choosing The Superior Parking Garage! Have a nice day!"
            self.parkingSpaces.append(space)
            self.parkingSpaces.sort()
            max_num= max(self.tickets)
            self.tickets.append(max_num + 1)
            del self.currentTicket[space]
            return farewell
        else:
            double_check = self.Payment(space)
        if double_check == 0:
            self.LeaveGarage()  

    def run_Parking_Garage(self):
        password = "alex"
        print('Welcome to "The Superior Parking Garage!\n Choose from the following options:\n')
        start = input('1: Take ticket\n\n2: Pay for parking\n\n'
        '3: Exit the garage\n\n\t(*For authorized users only*):\n\tEnter password shut down program\n\n'
        'What would you like to do?: ')
        clear_output()
        while True:
            if start.lower() == password:
                break
            elif start.lower() == '1':
                print(self.takeTicket())
                self.run_Parking_Garage()
            elif start.lower() == '2':
                print(self.payForParking())
                self.run_Parking_Garage()
            elif start.lower() == '3':
                print(self.LeaveGarage())
                self.run_Parking_Garage()
            else:
                print('Input not a valid response.Please enter "take"/"pay"/"exit".')
                self.run_Parking_Garage()

car = Parking_Garage()   
car.run_Parking_Garage()

