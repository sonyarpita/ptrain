class OwnIterator:
    def __init__(self,max):
        self.max=max
    def __iter__(self):
        self.initial=1
        return self
    def __next__(self):
        if self.initial <=self.max:
            x=self.initial
            self.initial+=1
            return x
        else:
            raise StopIteration
for x in OwnIterator(10):
    print("Num=",x)

'''class OwnIterator:
        def __init__(self,num=0):
                self.number=num
        def __iter__(self):
                self.x=1
                return self
        def __next__(self):
                if self.x<=self.number:
                        own_iterator=self.x
                        self.x+=1
                        return own_iterator
                else:
                        raise StopIteration
for x in OwnIterator(10):
        print("Num = ",x)
~
'''
