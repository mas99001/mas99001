class Stringdemo:
    def __init__(self):
        self.str = 'Interview int Kickstart int int'
        self.ntr = 'Interview Kickstart'
    def demonstration(self):
        self.standard()
        self.demo_search('int')
        self.demo_index('int')
    def standard(self):
        print('\n#### standard(self) ####'.upper())
        #print(f'{self.str.split()}')
        #print(*(range(len(self.str)))); print(*self.str)
        #print(*(f'{n:^3}' for n in range(len(self.str))),sep="")
        #print(*(f'{char:^3}' for char in self.str),sep="")
        print(f'upper():{self.str.upper()}')
        print(f'lower():{self.str.lower()}')
        print(f'capitalize():{self.str.capitalize()}')
        print(f'title():{self.str.title()}')
        print(f'swapcase():{self.str.swapcase()}')
        print(f'casefold():{self.str.casefold()}')

    def demo_search(self,sub):
        print('\n#### demo_search(self,sub) ####'.upper())
        print(f'find({sub} in {self.str}):Result: {self.str.find(sub)}')
        print(f'rfind({sub} in {self.str}):Result: {self.str.rfind(sub)}')
        print(f'count({sub} in {self.str}): Result: {self.str.lower().count(sub)}')

    def demo_index(self, sub):
        print('\n#### demo_index(self, sub) ####'.upper())
        try:
            result1 = self.str.index(sub)
        except ValueError:
            result1 = -1
        try:
            result2 = self.ntr.index(sub)
        except ValueError:
            result2 = -1
        print(f'index({sub} in {self.str}): Result: {result1}')
        print(f'index({sub} in {self.ntr}): Result: {result2}')

        print(f'{self.str} starts with {sub}?: {self.str.startswith(sub)}')
        print(f'{self.str} end with {sub}?: {self.str.endswith(sub)}')

        print(f'{self.ntr} starts with {sub}?: {self.ntr.startswith(sub)}')
        print(f'{self.ntr} end with {sub}?: {self.ntr.endswith(sub)}')
