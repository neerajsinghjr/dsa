from P027_While_Else import checkImport 
from resources.module  import divide
from copy import copy, deepcopy


def deep():
   list1 = [1,2,[4,5],5]
   list2 = copy(list1)
   print(f"list1-id: {id(list1)} list2-id: {id(list2)}")
   list1[3] = 10
   print(f"lis1: {list1} and list2: {list2}")
   list2[3] = 11
   print(f"lis1: {list1} and list2: {list2}")
   list1.append(12)
   list2.append(13)
   print(f"lis1: {list1} and list2: {list2}")
   print(f"list1-id: {id(list1)} list2-id: {id(list2)}")


def shallow():
   list1 = [1,2,[4,5],5]
   list2 = copy(list1)
   print(f"list1-id: {id(list1)} list2-id: {id(list2)}")
   list1[2][0] = 0
   list1[3] = 10
   print(f"lis1: {list1} and list2: {list2}")
   list2[2][1] = 0
   print(f"lis1: {list1} and list2: {list2}")
   list1.append(12)
   list2.append(13)
   print(f"lis1: {list1} and list2: {list2}")
   print(f"list1-id: {id(list1)} list2-id: {id(list2)}")


##---Main Execution;;
def main():
   print("#-------------- --shallow -------------#")
   shallow()
   # print("#-------------- --deep -------------#")
   # deep()
   # print("#-------------- --main  -------------#")
   # list1 = list2 = [1,2,[4,5],5]
   # print(f"list1-id: {id(list1)} list2-id: {id(list2)}")



if __name__ == '__main__':
    print("#------------ Code Start --------------#")
    main()
    print("#------------ Code Stop ----------------#")
    