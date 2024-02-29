def func_v1():
    # testing: nested for loops in list comprehension;;
    matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    ans = [num for row in matrix for num in row if num % 2]
    print("Odd Numbers: ", ans) # Odd Numbers: [1, 3, 5, 7, 9]
    ans = [ j for i in range(3) for j in range(3)]
    print(ans) # [0, 1, 2, 0, 1, 2, 0, 1, 2]


if __name__ == "__main__":
    func_v1()
