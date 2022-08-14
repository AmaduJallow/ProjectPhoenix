class Temperature:
    temp = 0

    def converter(self):
        self.temp = int(input("Please enter the temperature: "))
        _type = input("Please enter F for fahrenheit and C for Celsius: ")
        _type = _type.lower()
        if _type == "f":
            result = (self.temp - 32) * 5 / 9
            print(f"The {self.temp} F is {result}C")

        else:
            result = (self.temp * 9 / 5) + 32
            print(f"The {self.temp} C is {result}F")


TOFM = Temperature()
TOFM.converter()
