

class MyRange:
    step=1
    stop=0
    start=0
   
    def __init__(self,stop,start=0,step=1):
        self.start=start
        self.stop=stop
        self.step=step
        if self.step !=1 or self.start !=0:
            self.start,self.stop = self.stop,self.start
           
   
   
    def __iter__(self):
        if not self.valid():
            raise BaseException("Invalid interval!")
            return
        return self.__next__()
   
    def __next__(self):
        s = self.start
        if self.start <= self.stop:
            while s < self.stop:
                yield s
                s += self.step
        else:
            while s > self.stop:
                yield s
                s += self.step
   
   
   
           
    def valid(self):
        if (self.step==0) or (self.start > self.stop and self.step >= 0) or (self.start < self.stop and self.step <=0):
            return False
        else:
            return True
   
   
   
   
   



