class people:
    def __init__(self,name,gender,age):
        self.myname=name
        self.gender=gender
        self.age=age

    def onyesha(self):
        print(self.myname,self.gender,self.age)

# create an object
myobj=people("Riley","female",23)
myobj.onyesha()
myobj=people("Barry","male",29)
myobj.onyesha()
myobj=people("Tiana","female",19)
myobj.onyesha()