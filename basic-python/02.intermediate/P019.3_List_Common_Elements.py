# Program: to find common items from two lists.

try:
    # Check intersection between two list;
    def checkIntersection(firstList, secondList):
        firstSet = set(firstList)
        secondSet = set(secondList)
        values = firstSet.intersection(secondSet)
        if values:
            print("Intersecting Values ... \n", values)
        else:
            print("Sorry, No Intersecting Values Found !")


    # building program ladders;
    def makeProgram():
        temp = 0
        firstList = []
        secondList = []
        firstCount = int(input("Enter number of element in List A: "))
        secondCount = int(input("Enter number of element in List B: "))

        # Taking values of List A;
        for x in range(0, firstCount):
            temp = input("List A [%d]: " % (x + 1))
            firstList.append(temp)

        # Taking values in List B;
        for x in range(0, secondCount):
            temp = input("List B [%d]: " % (x + 1))
            secondList.append(temp)

        # Checking Intersection;
        checkIntersection(firstList, secondList)


    # main program execution;
    makeProgram()

except Exception as error:
    print("Exception Catched !")
    print("Exception: ", error)

finally:
    print("Thank You!")