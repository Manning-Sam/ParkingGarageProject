from typing import Type
from IPython.display import clear_output
from traitlets.traitlets import Instance

class Parking_Garage():
    def __init__(self):
        self.tickets = list(range(1,201))
        self.parkingSpaces = list(range(1,201))
        self.is_paid = False
        self.currentTicket = {}


    def takeTicket(self):
        input('Press enter to start')
        clear_output()
        if len(self.parkingSpaces) > 0:
            for i in range(1, len(self.tickets)):
                ticket = self.tickets.remove(i)
                space = self.parkingSpaces.pop(i)
                self.currentTicket[space] = self.is_paid 
                break
            return ticket
        else:
            print("Parking Garage is Full.")
            clear_output()
        


    def payForParking(self):
        space = input('Please enter your parking space number: ')
        clear_output()
        if space.isdigit() == False and space > 200 and space not in self.currentTicket:
            
            self.payForParking()
        else:
            space = int(space)

        flat_rate = 10


        
    def Payment(self, total, space):
        print('Your total is $' + str(total))
        amount = input('Please enter amount you are paying: ')
        if amount.isdigit() and int(amount) < total:
            total -= int(amount)
            print('Your total is now $' + str(total))
            clear_output()
            self.Payment(total, space)
        elif amount.isdigit() == False or int(amount) > total:
            print('Sorry that is not a valid number. Please Enter a valid number.')
            self.Payment(total,space)
        else:
            self.currentTicket[space] = True
            print('Thank you for your payment!')
            clear_output()

        
    def LeaveGarage():

