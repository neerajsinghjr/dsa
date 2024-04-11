## Program: Control Statement using List;
try:
    myList = [12, 15, 32, 42, 55, 75, 122, 132, 150, 100, 200]
    for x in myList:
        if x>120:
            break
        elif x%5 == 0:
            print("Your number: ", x)
        else:
            continue

except Exception as error:
    print("Something went wrong.", error)