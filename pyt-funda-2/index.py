import os
from string1 import Stringdemo as SD
from tuple import Tupledemo as TD
from dict import Dictdemo as DD
def clear_screen():
    # 'nt' means Windows, otherwise it's likely Linux or macOS
    os.system('cls' if os.name == 'nt' else 'clear')

clear_screen()
#std = SD()
#std.demonstration()
#ttd = TD()
#ttd.demo()
#ttd.func1()
#sdd = DD()
print(DD.twosum([1,2,3,4,5,6,7,8],10))
 ### check all the default functions for a class e.g. __init__ for cons, des, rep
 ## inheritance
 ## polymorphism
 #JSON load loads, dump, dumps