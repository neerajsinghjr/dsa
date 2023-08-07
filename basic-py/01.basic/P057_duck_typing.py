class Bird:
    def fly(self):
        print("fly with wings")
  
class Airplane:
    def fly(self):
        print("fly with fuel")
  
class Fish:
    def swim(self):
        print("fish swim in sea")
  
# Attributes having same name are
# considered as duck typing
for obj in Bird(), Airplane(), Fish():
    try:
        obj.fly()
    except Exception as e:
        print(f"{obj.__class__.__name__} can't fly")