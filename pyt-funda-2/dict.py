class Dictdemo:
    def __init__(self):
        self.lcount = {}
        self.ldata = [x**2 for x in range(1,10)]
    def func1(self):
        for x in self.ldata:
            if x in self.lcount:
                self.lcount[x] +=1
            else:
                self.lcount[x] = 1
        print(self.lcount)
        print(self.ldata)
    @staticmethod
    def twosum(nums, target):
        print(f'nums: {nums}')
        print(f'targer is: {target}')
        ind1 = 0
        ind2 = 0
        for i in range(0,len(nums)):
            for j in range(i+1,len(nums)):
                print(nums[i], nums[j],target)
                if((nums[i] + nums[j]) == target):
                    return(i,j)
        return(-1,-1)