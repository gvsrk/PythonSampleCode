

class sampleclass:
    name='rama krishna'
    pin=500062
    
    def printname(self):
        print('my name',self.name)
    
    def printaddress(self):
        print ('my address',self.pin)
        
def callingfunc():
    objsampleclass = sampleclass()
    print('entered')
    objsampleclass.printname()
    objsampleclass.printaddress()
    
callingfunc()
        