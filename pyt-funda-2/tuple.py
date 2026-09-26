class Tupledemo:
    def __init__(self):
        self.tup = (1,2,3,4,"kap",4.0)
    def demo(self):
        print('\n#### demo(self) ####'.upper())
        a,b,c,d,e,f = self.tup
        #self.tup[0] = 11
        print(f'{self.tup} is whole tuple')
        print(f'{a} is same as {self.tup[0]}')
        print(f'{b} is same as {self.tup[1]}')
        print(f'{c} is same as {self.tup[2]}')
        print(f'{d} is same as {self.tup[3]}')
        print(f'{e} is same as {self.tup[4]}')
        print(f'{f} is same as {self.tup[5]}')
    def func1(self):
        self.s1 = set(self.tup)
        self.s1.add(10)
        self.s1.add(5)
        print(f'{self.s1} is the corresponding set:Note that 4.0 is gone')
