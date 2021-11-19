print("-----------------------------------CODE BEGINS ---------------------------------------")

## Python Oops;

##--- Name Mangling;
# class student:
#     def __init__(self, name, enroll):
#         self.__name = name
#         self.enroll = enroll

# neeraj = student("neeraj", 176096879)
# print(neeraj.__name)                              ## private variable
# print(neeraj.enroll)                              ## non-private variable
# print(neeraj._student__name)                      ## name mangling, accessing private using _classname;
# print(dir(neeraj))


# class Map: 
#     def __init__(self): 
#         self.__geek() 
#         # print("geek:",geek)
          
#     def geek(self): 
#         print("In parent class") 
    
#     # # private copy of original geek() method 
#     # __geek = geek    
    
# class MapSubclass(Map): 
#     # provides new signature for geek() but 
#     # does not break __init__() 
#     def geek(self):             
#         print("In Child class")
          
# # Driver's code
# obj = MapSubclass()
# obj.geek()


# ## public access modifier --class;
# class student:
#     def __init__(self, name1, name2):
#         self.name1 = name1
#         self.name2 = name2
    
#     def show(self):
#         print("first:", self.name1)
#         print("last:", self.name2)
        
# neeraj = student("neeraj","singh")
# neeraj.show()


# ## protected access modifiers --class
# class Father:

#     def __init__(self, run, power, brain):
#         self._run = run
#         self._brain= brain
#         self._power = power

#     def showPowers(self):
#         print("Run:", self._run)
#         print("Brain:", self._brain)
#         print("Power:", self._power)


# class Son(Father):

#     def __init__(self, run, brain, power, jump):
#         Father.__init__(self, run, brain, power)
#         self._jump = jump
    
#     def showNewPowers(self):
#         self.showPowers()
#         print("Jump:", self._jump)

# xerus = Son("1000KM/PH", "1000 IQ", "10,000 Amp", "500 KM")
# xerus.showNewPowers()


print("-----------------------------------CODE ENDS ---------------------------------------")