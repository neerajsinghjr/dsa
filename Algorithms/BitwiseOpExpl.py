

# GET NUMBER
def getNumber(Message=None):
    if Message:
        return int(input(Message))

    return int(input("Number: "))


# CHECK EVEN OF ODD;
def checkEvenOrOdd():
    number = [12, 13, 141, 41, 51, 5, 166, 66]
    if not evenOrOdd(number):
        print("Something Went Wrong, please check ...")


# GET BIT NUMBER;
def getBitNumber(number=None, shift=None):
    if not (number and shift >= 0):
        number = getNumber()
        shift = int(input("Shift: "))
    bit = getBit(number, shift)
    if bit != None:
        print(f"Bit: {bit}")
    else:
        print(f"Something Went Wrong")


# SET BIT NUMBER;
def setBitNumber(number=None, position=None):
    if not (number and (position >= 0)):
        number = getNumber()
        position = int(input("Position: "))

    result = setBit(number, position)
    if result != None:
        print(f"Before: {number}")
        print(f"After: {result}")
    else:
        print("Something Went Wrong")


# CLEAR BIT NUMBER;
def clearBitNumber(number=None, position=None):
    if not (number and (position >= 0)):
        number = getNumber()
        position = int(input("Position: "))

    result = clearBit(number, position)
    if result != None:
        print(f"Before: {number}")
        print(f"After: {result}")
    else:
        print("Something Went Wrong")


# UPDATE BIT NUMBER;
def updateBitNumber(number=None, position=None, value=None):
    if not (number and position and value):
        number = getNumber()
        position = int(input("Position: "))
        value = int(input("Value: "))

    result = updateBit(number, position, value)
    if result != None:
        print(f"Before: {number}")
        print(f"After: {result}")
    else:
        print("Something Went Wrong")


# CLEAR ALL BIT TILL 'K' LOCATION;
def clearKthBit(number=None, position=None):
    if not (number and position):
        number = getNumber()
        position = int(input("Position: "))

    result = clearBitTillPosition(number, position)
    if result != None:
        print(f"Before: {number}")
        print(f"After: {result}")
    else:
        print("Something Went Wrong")


## CLEAR ALL BIT FROM START TO END;
def clearBitRange(number=None, start=None, end=None):
    if not (number and start and end):
        number = getNumber()
        start = getNumber("Start: ")
        end = getNumber("End: ")

    result = removeBitRange(number, start, end)
    if result != None:
        print(f"Before: {number}")
        print(f"After: {result}")
    else:
        print("Something Went Wrong")


## COUNT SET BIT HACK IN A NUMBER;
def countSetBitHack(number=None):
    if not (number == None):
        number = getNumber()
    result = countBitHack(number)
    if result != None:
        print(f"Set Bits: {result} --HACK")
    else:
        print("Something Went Wrong")


## COUNT SET BIT IN A NUMBER;
def countSetBit(number=None):
    if not (number == None):
        number = getNumber()
    result = countBit(number)
    if result != None:
        print(f"Set Bit: {result}")
    else:
        print("Something Went Wrong")


## MAIN EXECUTION;
def main():
    """
    BITWISE OPERATION FUNCTIONS...
    checkEvenOrOdd()		        ## Check Even or Odd;
    getBitNumber()				    ## GET A SPECIFIC BIT NUMBER;
    setBitNumber()				    ## SET A PARTICULAR BIT NUMBER;
    clearBitNumber( '')			    ## CLEAR A SPECIFIC BIT NUMBER;
    updateBitNumber()			    ## UPDATE A SPECIFIC BIT NUMBER;
    clearKthBit()				    ## CLEAR ALL BIT TILL 'K' LOCATION;
    clearBitRange()				    ## BIT FROM INDEX START TO END;
    countSetBitHack(21)			    ## CLEAR SET BIT HACK
    countSetBit(21)				    ## CLEAR SET BIT
    print(powerOfTwo(16))			## POWER OF TWO;
    print(fastExpo(num=2, pow=5))	## FAST EXPONENTIAL FOR A NUMBER;
    print(convertIntToBin(8))
    print("Program Terminated!")
    """
    print(flip32BitInterger(9))    
    print(flipAllBits(-9))


if __name__ == "__main__":
    main()

    