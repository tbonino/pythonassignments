#Variables
farhenheit = float()
celcius = float()
Continue = str()

#loop
while Continue != "Q":
  #input
  farhenheit = float(input("Degrees Fahrenheit:"))
  celcius = (farhenheit-32)*(5/9)
  print("Degrees Celsius:", celcius)
  Continue = str(input("Continue:"))
