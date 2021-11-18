## Program: Print the union and intersection of all even and odd [0, 20]
try:
    even = set()
    odd = set()

    for x in range(0, 21):
        if x % 2 == 0:
            even.add(x)
        else:
            odd.add(x)

    print("Union: ", even | odd)
    print("Intersection: ", even & odd)

except ValueError:
    print("Something unexcepected occurred ...")

finally:
    print("Thank you !")
