## Program: Write a Python to print this pattern:
# 55555
# 4444
# 333
# 22
# 1

try:
    for x in range(5, 0, -1):
        for y in range(0, 5):
            if (y < x):
                print(x, end=" ")
        print()

except Exception as error:
    print("Unhandled Exception: ", error)
