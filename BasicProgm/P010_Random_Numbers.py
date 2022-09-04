## Program: Generate 6 random numbers between 1 to 6;

import random

try:
    randList = []
    for x in range(0, 6):
        temp = random.randint(1, 6)
        randList.append(temp)
        print("Iteration %d: %d" % (x + 1, temp))
    print("Random List: ", randList)

except Exception as error:
    print("Unhandled exception occurred.", error)



