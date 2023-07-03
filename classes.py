class Magari:
    def __init__(self,modelname,color,year,capacity):
        self.model=modelname
        self.mycolor=color
        self.myyear=year
        self.mycapacity=capacity
    def onyesha(self):
        print(self.model,self.mycolor,self.myyear,self.mycapacity)
# create an object
myobj=Magari("Toyota","White",2020,"2500cc")
myobj.onyesha()