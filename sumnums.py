class SumNums():
    def __init__(self,nums,target):
        self.nums=nums
        self.target=target
        numbers=[]
        index=[]
        for i in self.nums:
            numbers.append(i)
        numbers.sort()
        numbers.reverse()
        for i in numbers:
            if self.target-i>=0:
                for j in self.nums:
                    if i==j:
                        index.append(self.nums.index(j))
                self.target-=i
        index.sort()
        for i in index:
            print('index-',i)
print(SumNums([2,4,3,1],7))