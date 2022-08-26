## Program: Find out the largest word in the string "This is an umbrella";
try:
    # Helping Variables;
    string = input("Your String: ")
    splitArray = string.split(" ")
    maxLen = []
    maxValue = []

    # Logic implementations;
    for x in splitArray:
        if len(maxLen) == 0 and len(maxValue) == 0:
            maxValue.append(x)
            maxLen.append(len(x))
        else:
            if maxLen[0] < len(x):
                maxLen.clear()
                maxValue.clear()
                maxLen.append(len(x))
                maxValue.append(x)

            elif maxLen[0] == len(x):
                maxLen.append(len(x))
                maxValue.append(x)

            else:
                continue

    # Iterating over two list together;
    for x, y in zip(maxValue, maxLen):
        print("Max Value: %s with Length: %d" % (x, y))

except Exception as error:
    print("Unhandled Exception.", error)