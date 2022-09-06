import re


def validateEmail(email):
    if(len(email) > 3):
        return bool(re.match("^.+@(\[?)[a-zA-Z0-9-.]+.(a-zA-Z){2-3}|[0-9]{1,3})(]?)$",email))
    return False

def checkEmail():
    email = "Neeraj@gmail.com"
    if validateEmail(email):
        print("Valid")
    else:
        print("Invalid")
    

def main():
    checkEmail()
    # name = "maj"
    # result = re.match("[a-z]",name)
    # result = re.match(".",name)
    # result = re.match("[0-9]&",name)
    # result = re.match("ma*.n",name)                           ## one character valid in-place of *
    # result = re.match("n.*.j",name)                         
    # print(result)   


if __name__ == "__main__":
    print("#------------- Code Start -----------------#")
    main()
    print("#------------- Code Ends  -----------------#")





