## Program: Generate list of 20 Prime Numbers;
def generatePrime():
    prime = []
    for x in range(2, 100):
        count = 0
        if len(prime) == 20:
            return prime
        else:
            for y in range(1, x+1):
                # if count is not more than 3
                if x%y == 0:
                    count = count + 1

            # Check if count is less than 3
            if count < 3 and count != 0:
                prime.append(x)

    return prime

prime = generatePrime()
print("Prime List: ", prime)
print("Prime List Type: ", type(prime))
