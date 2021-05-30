##A good friend of yours owns a small company that produces a tool the helps disabled individuals open jars and containers. Rather than buy a time clock mechanism, he would like to put an old computer on the warehouse floor that could be used as the time clock and help them manage materials, shipments, etc. Your friend was able to find an inexpensive application to keep track of each employee’s hours. However, this application did not contain the code to determine how much each employee needs to get paid at the end of the week. Therefore, he has come to you for some help. He would like you to develop a small application that would accept the total number of hours worked and the hourly rate for his employees. The program would then calculate the total pay. You will need to use the following equations to determine net pay:
##Gross Pay = Hours Worked * Pay Rate
##Deductions = Gross Pay * 0.35
##Net Pay = Gross Pay – Deductions
##Create a class to solve the problem listed above. Name your class NetPay. Your class will need the number of hours worked and the pay rate when the object is created. Your class will need to store these values in attributes called: hours and rate. Additionally your class will need to return the gross pay, the amount in deductions and net pay. Store these values in attributes called gross, deductions and net. In order to create these values you will need to write the following methods: GetGrossPay, GetDeductions and GetNetPay. Within these methods, your code will perform the appropriate calculation and return the value generated. In the GetNetPay method you will need to call the the GetGrossPay and GetDeductions methods. To do this you will need to enter the following code:
##self.GetGrossPay()
##self.GetDeductions()
##When creating this class you may want to start coding in VS Code or Python. After you have coded your class, create an object to test your class. If you send in 20 for hours worked and 15 for rate, when you call your methods and print them, your program will print out the following:
##300
##105.0
##195.0

class NetPay:
    def __init__(self, hours, rate):
        self.hours = hours
        self.rate = rate
        self.gross_pay = float()
        self.deductions = float()
        self.net_pay = float()

    def GetGrossPay(self):
        self.gross_pay = self.rate * self.hours
        return self.gross_pay
        
    def GetDeductions(self):
        self.deductions = self.gross_pay * 0.35
        return self.deductions

    def GetNetPay(self):
        self.net_pay = self.GetGrossPay() - self.GetDeductions()
        return self.net_pay

#deleted main in Codio and it accepted it for a full grade
def main():
    hours_worked = int()
    pay_rate = float()
    hours_worked = int(input())
    pay_rate = float(input())
    my_net_pay = NetPay(hours_worked, pay_rate)
    print(my_net_pay.GetGrossPay())
    print(my_net_pay.GetDeductions())
    print(my_net_pay.GetNetPay())

main()
