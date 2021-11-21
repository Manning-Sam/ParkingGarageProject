# # from typing import Type
# # from IPython.display import clear_output
# # from traitlets.traitlets import Instance

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
                self.tickets.remove(i)
                space = self.parkingSpaces.pop(i)
                self.currentTicket[space] = self.is_paid 
                break
            return space
        else:
            print("Parking Garage is Full.")
            clear_output()
        


    def payForParking(self):
        space = input('Please enter your parking space number: ')
        clear_output()
        if space.isdigit() == False and space > 200 and space not in self.currentTicket:
            print('Sorry that is not a valid number. Please Enter a valid number.')
            self.payForParking()
        else:
            space = int(space)

        flat_rate = 10
        payment= self.Payment(flat_rate, space)
        if payment != 0:
            print("Your total is now $" + str(payment))
            return payment
        else:
            print('Thank you for your payment!')
            clear_output()
            return space
        
    def Payment(self, total, space):
        print('Your total is $' + str(total))
        amount = input('Please enter amount you are paying: ')
        if amount.isdigit() and int(amount) < total:
            total -= int(amount)
            return total
        elif amount.isdigit() == False or int(amount) > total:
            print('Sorry that is not a valid number. Please Enter a valid number.')
            self.Payment(total,space)
        else:
            self.currentTicket[space] = True
            

        
    def LeaveGarage(self, total=0):
        space = input('Please enter your parking space number: ')
        space= int(space)
        if self.currentTicket[space] == True:
            print("Thanks! Have a nice day!")
            self.parkingSpaces.append(space)
            self.parkingSpaces.sort()
            max_num= max(self.tickets)
            self.tickets.append(max_num + 1)
            del self.currentTicket[space]
        else:
            total += int(total)
            self.Payment(self, total, space)



