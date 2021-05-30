#GetCelsius function
def GetCelsius(fahrenheit):
  degrees_celsius = (fahrenheit-32)*0.5556
  degrees_celsius = int(degrees_celsius)
  return degrees_celsius

#GetMeters function
def GetMeters(feet):
  number_of_feet = int(feet)
  number_of_meters = number_of_feet * 0.3048
  return number_of_meters

#Define main here
def main():
  fahrenheit = int()
  feet = int()
  degrees_celsius = int()
  number_of_meters = int()
  fahrenheit = int(input("Enter degrees Fahrenheit:  "))
  feet = int(input("Enter feet:  "))
  degrees_celsius = GetCelsius(fahrenheit)
  print("Degrees Celsius:  ", degrees_celsius)
  number_of_meters = GetMeters(feet)
  print("Meters:  ", number_of_meters)

main()
