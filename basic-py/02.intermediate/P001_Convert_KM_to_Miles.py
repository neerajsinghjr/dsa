# Program: Convert Kilo To Miles;
def changeKiloToMiles(number):
    return number * 0.621371

try:
    number = int(input("Enter KM: "))
    print("Miles: ", changeKiloToMiles(number))

except ValueError:
    print("Something unexcepted occured ...")