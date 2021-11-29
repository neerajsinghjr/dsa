import re


def main():
    name = "maj"
    # result = re.match("[a-z]",name)
    # result = re.match(".",name)
    # result = re.match("[0-9]&",name)
    result = re.match("ma*.n",name)                           ## one character valid in-place of *
    # result = re.match("n.*.j",name)                         
    print(result)   


if __name__ == "__main__":
    print("#------------- Code Start -----------------#")
    main()
    print("#------------- Code Ends  -----------------#")





