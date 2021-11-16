## Program: Define calculation(), accept two variable return addition and subtraction of it.

try:
    def calculation(a, b):
        add = a+b
        sub = a-b
        return [add, sub]

    # Input Values
    a = int(input("Enter value a: "))
    b = int(input("Enter value b: "))

    dic = calculation(a, b)

    print(dic, type(dic))
    print("Addition: ", dic[0])
    print("Subtraction: ", dic[1])

except Exception as error:
    print("Exception caught ", error)

finally:
    print("Thank you!")
