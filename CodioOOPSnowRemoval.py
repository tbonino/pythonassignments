##Create a class called SnowRemoval. This class will utilize a constructor so that the class can obtain the size of the sidewalk that needs to be plowed along with any driveways. The size of the sidewalk is measured in feet and needs to be saved as a float. The number of driveways will be saved as an integer. Within your class store these values in attributes called sidewalk and driveway. Your class will need a method to calculate how much it will cost to have the snow removed on a property. This calculation will take the size of the sidewalk, measured in feet, and multiply it by 5. Meaning it will cost 5 dollars a foot to have your snow shoveled.
##Additionally you will include an extra cost if there is a driveway. If there is no driveway then the cost is 0. If there is a one car driveway the price to plow the driveway is 10 dollars. If the driveway is for 2 cars, the cost to plow the driveway is 20 dollars. If there are 3 or more cars the cost will be 30 dollars. Finally, if there are 4 or more driveways the cost is 50 dollars.
##Store the total cost in an attribute called total. Name this method CalculateTotal. In order to allow the total cost to leave the class, you will need to create a second method called ReturnTotal. All this method does is return the total.
##When creating this class start coding in VS Code or IDLE. To test your class create an object. Send in the values 15 and 2 (15 feet and 2 car driveway). Next call your method CalculateTotal. Finally print the method ReturnTotal to the screen. Your code should print the following:
##95

class SnowRemoval:
    def __init__(self, sw_size, num_driveways):
        self.sidewalk = float()
        self.driveway = int()
        self.sidewalk = sw_size
        self.driveway = num_driveways
        self.sw_charge = float()
        self.dw_charge = int()
        self.total = float()

    def SidewalkCharge(self):
        self.sw_charge = self.sidewalk * 5
        return self.sw_charge

    def DrivewayCharge(self):
        if self.driveway == 1:
            self.dw_charge = 10
        elif self.driveway == 2:
            self.dw_charge = 20
        elif self.driveway == 3:
            self.dw_charge = 30
        elif self.driveway >= 4:
            self.dw_charge = 50
        else:
             self.dw_charge = 0
        return self.dw_charge

    def CalculateTotal(self):
        self.total = self.SidewalkCharge() + self.DrivewayCharge()
        return self.total

    def ReturnTotal(self):
        return self.CalculateTotal()

def main():
    size = float()
    num = int()
    size = float(input())
    num = int(input())
    my_charge = SnowRemoval(size, num)
    my_charge.CalculateTotal()
    total = my_charge.ReturnTotal()
    print(total)

main()
