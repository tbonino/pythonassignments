class Bike:
  def __init__(self):
    tires = str()
    color = str()
    num_speeds = int()
    
  def MoveForward(self):
    print("Moving Forward")
  
  def Brake(self):
    print("STOP")
    
  def TurnRight(self):
    print("Turning Right")
  
  def TurnLeft(self):
    print("Turning Left")

MyRedBike = Bike()

MyRedBike.color = "red"
MyRedBike.tires = "fat tires"
MyRedBike.num_speeds = 7
MyRedBike.MoveForward()
MyRedBike.TurnRight()
MyRedBike.TurnLeft()
MyRedBike.Brake()

print(MyRedBike.color)
print(MyRedBike.tires)
print(MyRedBike.num_speeds)
