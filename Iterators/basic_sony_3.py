class OwnIterator:
    def __init__(self,num): #max value
        self.end=num
    def __iter__(self): #initialize
        self.num=1
#        print("Value of self.num=",self.num)
        return self
    def __next__(self): #how iteration shud happen
#        print("Value of self.num=",self.num)
#        print("Value of Max =",self.end)
        if self.num <= self.end:
            iterx=self.num
            self.num+=1
            return iterx
        else:
            raise StopIteration

for x in OwnIterator(10):
    print("X=",x)

