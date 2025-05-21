from modules.testmodule import MyClass,add
from modules.CustomList import Modifyed_list

l1=Modifyed_list()

obj1=MyClass()
print(obj1.__mymind__())
print(add(4,6))

l1.append(1)
l1.append(2)
l1.append(3)
l1.append(100,0)
l1.append(90)
print(l1)