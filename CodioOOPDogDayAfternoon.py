##Many dog owners see the benefit of buying natural dog food and treats. Dog Day Afternoon is a local company that creates its own dog food and treats. Their products are made locally and with natural ingredients. Sales are up and the owners of Dog Day Afternoon have decided to expand their business. Currently they are manually calculating sales. They need a computer program to help speed up the process.
##The owners of Dog Day Afternoon decided to get some help. They approached the Career Center and posted numerous temporary programming positions. You are eager to get some experience as a programmer so you apply and get the job.
##Your portion of the project is to create a class called DogDay that will take in the quantity and the size of the dog treat. Store these values in attributes called quantity (integer) and size (string). The class will also contain three methods. One method will determine the cost of one dog bone. Name this method DeterminePrice. The cost of the different size natural raw hide bones is as follows:
##Size A = $2.29
##Size B = $3.50
##Size C = $4.95
##Size D = $7.00
##Size E = $9.95
##Store the cost of each individual dog bone in an attribute called price.
##Your second method will be called DetermineTotal. This method will calculate the total cost (quantity * cost) and round this value to 2 decimal places. It will store this value in an attribute called total.
##Your final method will return the total.
##When creating this class start coding in VS Code or IDLE. To test your class create an object. Send in the values 6 and C. Next call your method DeterminePrice followed by DetermineTotal. Finally print the method ReturnTotal to the screen. Your code should print the following:
##29.7

class DogDay:
    def __init__(self, treat_num, treat_size):
        self.quantity = int()
        self.size = str()
        self.quantity = treat_num
        self.size = treat_size
        self.price = float()
        self.total = float()

    def DeterminePrice(self):
        if self.size == "A":
            self.price = 2.29
        elif self.size == "B":
            self.price = 3.50
        elif self.size == "C":
            self.price = 4.95
        elif self.size == "D":
            self.price = 7.00
        elif self.size == "E":
            self.price = 9.95
        else:
            self.price = 0
        return self.price

    def DetermineTotal(self):
        self.total = self.DeterminePrice() * self.quantity
        return self.total

    def ReturnTotal(self):
        return round(self.DetermineTotal(),2)

def main():
    num = int()
    size = str()
    num = int(input("How many treats would you like? "))
    size = input("What size? Choose A, B, C, D or E: ")
    my_treat = DogDay(num, size)
    print(my_treat.ReturnTotal())

main()
        
