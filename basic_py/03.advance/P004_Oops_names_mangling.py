'''
-------------------------------------------------------------------------------------
-> Title:  Name Mangling
-> Attempted: 10/03/2023
-> Description: 
-------------------------------------------------------------------------------------

Name Mangling 

-------------------------------------------------------------------------------------
'''

from time import time


class User:

    def __foo():
        print("Foo Called")

    @classmethod
    def bar(cls):
        print("Bar called ")


##---Main Execution;;
def main():
    # Private method called directly: Throw Error;;
    User._User__foo()

    # # Name Mangling : Basically changing the name of the private method __foo() into _User__foo();;
    # User._User__foo()

    # Class method calling;;
    User.bar()


if __name__ == '__main__':
    print("#------------ Code Start --------------#")
    startTime = time()
    main()
    endTime = time()
    print("Run Time:",endTime-startTime,"ms")
    print("#------------ Code Stop ----------------#")