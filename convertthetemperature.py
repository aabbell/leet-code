def convertTemperature(self,celsius):
    ans = []
    kelvin = celsius + 273.15
    ans.append(kelvin)
    fahrenheit = celsius * 1.80 + 32.00
    ans.append(fahrenheit)
    return ans