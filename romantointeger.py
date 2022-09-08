class RomanToInteger():
    def __init__(self,nums):
        self.nums=nums
        result=0
        x=2000
        numbers=[]
        for i in self.nums:
            if i=='I':
                i=1
            elif i=='V':
                i=5
            elif i=='X':
                i=10
            elif i=='L':
                i=50
            elif i=='C':
                i=100
            elif i=='D':
                i=500
            elif i=='M':
                i=1000
            numbers.append(i)
        for i in numbers:
            if i<=x:
                x=i
                result+=x
            else:
                x=i
                result=x-result
        print(result)
RomanToInteger('XXXL')