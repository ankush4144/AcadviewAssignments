class Temperature:
    def convertFarenheit(self,c):
        print("Temp in \N{DEGREE SIGN}F",c*1.8+32)
        
    def convertCelcius(self,f):
        print("Temp in \N{DEGREE SIGN}C",(f-32)*(5/9))
temp=Temperature()
temp.convertFarenheit(int(input("Enter temp in celcius to convert to farenheit")))
temp.convertCelcius(int(input("Enter temp in farenheit to convert to celcius")))
