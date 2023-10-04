def celsiusToFahrenheit(tempCelsius):
    tempFahrenheit = 9 / 5 * tempCelsius + 32
    return tempFahrenheit

def fahrenheitToCelsius(tempFahrenheit):
    tempCelsius = 5 / 9 * (tempFahrenheit - 32)
    return tempCelsius

temp = float(input("Enter a temperature: "))
if input("(1) Convert to Celsius \n(2)Convert to Fahrenheit\nEnter 1/2: ") == "1":
    print(float(fahrenheitToCelsius(temp)))
else:
    print(float(celsiusToFahrenheit(temp)))