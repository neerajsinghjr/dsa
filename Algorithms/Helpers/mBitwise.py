"""
 BITWISE OPERATION FILE: MAINTAINING CRUD BITWISE OPERAITON;

"""


def getBit(number, shift):
    """
    GET_BIT: RETURN PARTICULAR BIT OF NUMBER PLACED AT 'i' POSITION;
    """
    if number and shift >= 0:
        mask = number >> shift
        return (mask & 1)
    else:
        return None


def setBit(number, position):
    """
    SET_BIT: RETURN PARTICULAR BIT OF NUMBER PLACED AT 'i' POSITION;
    """
    if number and (position >= 0):
        mask = 1 << position
        return (mask | number)
    else:
        return None


def clearBit(number, position):
    """
    CLEAR_BIT: CLEAR PARTICULAR BIT OF NUMBER PLACED AT 'i' POSITION;
    """
    if number and (position >= 0):
        mask = ~(1 << position)
        return mask & number
    else:
        return None


def updateBit(number, position, value):
    """
    UPDATE_BIT: UPDATE PARTICULAR BIT OF NUMBER PLACED AT 'i' POSITION;
    """
    if (number and (position >= 0) and (value == 0 or 1)):
        ## Mask that ha set bit at particular place;
        mask = ~(1 << position)
        return (number & mask | value << position)
    else:
        return None


def clearBitTillPosition(number, position):
    """
    CLEAR_BIT_TILL_POSITION: DELETE ALL BIT TILL POSITION 'K';
    """
    if (number and (position >= 0)):
        mask = -1 << position
        return mask & number
    else:
        return None


def removeBitRange(number, start, end):
    """
    REMOVE_BIT_RANGE: DELETE ALL BIT FROM INDEX START TO END;
    """
    if (number and start >= 0 and end >= 0):

        leftMask = ~0 << end + 1

        rightMask = (1 << start) - 1

        mask = leftMask | rightMask

        return mask & number
    else:
        return None


## COUNT THE SET BIT IN NUMBER HACK;
def countBitHack(number):
    if number != None:
        count = 0
        while (number > 0):
            number = (number & number - 1)
            count += 1

        return count
    else:
        return None


## COUNT THE SET BIT IN NUMBER;
def countBit(number):
    if number != None:
        count = 0
        while (number > 0):
            count += number & 1
            number = number >> 1

        return count
    else:
        return None


## POWER OF 2
def powerOfTwo(number):
    if number == 0:
        return 0
    elif number > 0:
        if (number & number - 1) == 0:
            return True
        return False
    else:
        return False


## FAST EXPONENTIAL OF NUMBER;
def fastExpo(num, pow):
    if (num and pow):
        result = 1  # result = 1
        while (pow > 0):
            lastBit = (pow & 1)  # bit = 11001
            if lastBit:
                result = result * num
            num = num * num
            pow = (pow >> 1)

        return result
    else:
        return None


## CONVERT INTEGER TO BINARY;
def convertIntToBin(number):
    base = 10
    pow = 1
    result = 0
    while (number > 0):
        lastBit = number & 1  ## Taking Out Last Bit;
        result += lastBit * pow
        pow = pow * base
        number = number >> 1  ## Removing Bits From Left;
    print(result)


## CHECK EVEN OR ODD IN NUMBER;

def evenOrOdd(number=None) -> bool:
    """
    Even or Odd - Based on Bitwise Manipulation
    """
    dataType = type(number)
    if dataType == list:
        for num in number:
            if (num & 1):
                print(f"Num {num} is Odd")
            else:
                print(f"Num {num} is Even")
    elif dataType == int:
        if (number & 1):
            print(f"Num {number} is Odd")
        else:
            print(f"Num {number} is Even")
    else:
        return False

    return True