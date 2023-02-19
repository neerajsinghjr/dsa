print("-----------------------------------CODE BEGINS ---------------------------------------")


# ## Global Variable...
# a = 1
# b = 1
# def func1():
#     global a
#     print(a)
#     a += 1
#     print(a)
# func1()
# print("after...")
# print(a)

# ## accessing global variable using global methods
# globalList = globals()
# print(globalList['a'])

# ## multiple assignments
# a,b,c = 1,2,3
# print(a,b,c)
# a=1, b=2, c=3
# print(a,b,c)

# ## VARIABLE SCOPE
# ##--- Local scope & Global Scope;
# a = 2           # global scope
# def cal():
#     a = 3       # local scope
#     return (a*a)
# print(cal())
# print(a*a)

# ##--- Enclosing Scope 
# a = 10                      # Global Scope;
# def cal():
#     b = 4                   # Enclosed Scope: Neither Local or Global;
#     def sqrt():
#         b = 5               # local scope
#         return (b*b)
#     def sum():
#         b = 6               # Local Scope
#         return (b+b)
#     print(sqrt(),sum())
# cal()

# ## FUNCTION CALLS;
# def cal():
#     var = 25*25
#     print("from cal:", var)
#     return var
    
# print("cal without ():", cal)
# x = cal
# print("from x:", x())


# NON-KEYWORDED ARGUMENTS
def calc(*args):
    print(type(args))                                           ## tuple
    for (key, value) in enumerate(args):
        print(key,"=>", value)

calc("Hi", "Neeraj","Singh")
calc(text="Hi", firstName="Neeraj", lastName="Singh")           ## attribute error

# ## KEYWORDED-ARGUMENTS
# def calc(**kargs):
#     print(type(kargs))                                         ## dict
#     for (key,value) in kargs.items():
#         print(key,"=>",value)

# # calc("Hi", "Neeraj","Singh")                                 ## attribute error;
# calc(text="Hi", firstName="Neeraj", lastName="Singh")

print("-----------------------------------CODE ENDS ---------------------------------------")