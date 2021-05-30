class Dog:
    def __init__(self, myweight, mycolor, mydob, mybreed):
        self.weight = myweight
        self.color = mycolor
        self.dob = mydob
        self.breed = mybreed
        self.message = str()

    def Fetch(self):
        self.message = "my dog is fetching a stick"
        return self.message

    def Bark(self):
        self.message = "woff"
        return self.message

    def Run(self):
        self.message = "my dog is running"
        return self.message

    def Sleep(self):
        self.message = "zzzzzzzzzzzzzzz"
        return self.message

#Creating the object
Rover = Dog(72, "yellow", "03-12-2009", "Labrador")
#Using the methods
print(Rover.Bark())
print(Rover.Fetch())
print(Rover.Run())
print(Rover.Sleep())
