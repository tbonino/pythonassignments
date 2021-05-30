##Create a class called GymMembership that takes in the number of Gym Memberships and the type. Using a constructor, assign two attributes to the number of memberships and type. Within this class add three methods: DetermineRate, DetermineTotal and ReturnTotal. DetermineRate will find the cost of the membership based on the type of membership the user wants. It will store this value in the attribute rate. The “bronze” membership is 25 dollars a month, the “silver” membership is 35 dolars a month, the “gold” membership is 50 dollars a month and the “platinum” is 75 dollars a month. The method DetermineTotal will use the cost of one membership and multiply it by the number of memberships. It will store this value in an attribute called total. At this gym customers agree to a one year contract. Therefore the total is going to be for the year and not the month. Finally the ReturnTotal method returns the total cost for the membership.
##When creating this class start coding in VS Code or IDLE. To test your class create an object. Send in the values 5 and silver. Next call your method DetermineRate followed by DetermineTotal. Finally print the method ReturnTotal to the screen. Your code should print the following:
##2100

class GymMembership:
    def __init__(self, member_num, member_type):
        self.mem_num = member_num
        self.mem_type = member_type
        self.rate = int()
        self.total = int()

    def DetermineRate(self):
        if self.mem_type == "bronze":
            self.rate = 25
            return self.rate
        elif self.mem_type == "silver":
            self.rate = 35
            return self.rate
        elif self.mem_type == "gold":
            self.rate = 50
            return self.rate
        elif self.mem_type == "platinum":
            self.rate = 75
            return self.rate
        else:
            return self.rate

    def DetermineTotal(self):
        self.total = self.mem_num * self.DetermineRate() * 12
        return self.total

    def ReturnTotal(self):
        return self.DetermineTotal()

def main():
    num = int()
    membership = str()
    num = int(input("How many memberships (in whole numbers)?: "))
    membership = input("Pick a membership: bronze, silver, gold or platimum: ")
    my_gym = GymMembership(num, membership)
    print(my_gym.ReturnTotal())

main()
        
        
