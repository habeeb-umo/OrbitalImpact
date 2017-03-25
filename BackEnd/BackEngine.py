from SolarSystem import SolarSystem
from GUI import Button
from GUI import ScreenText

def main():
    BackEngine()

class BackEngine:

    def __init__(self, backEngine):
        self.BE=backEngine
        self.turn=0
        self.solSystem=SolarSystem(self)
        self.vesselList=[]
        self.testButton=Button(self.BE,0,0, self.printTest)
        self.testButton2 = Button(self.BE, 22, 11, self.printTest)
        self.testText = ScreenText(self.BE,0,0,0,0,"Hello world")

    def printTest(self):
        print "Hello, from BackEngine"

    def runTurn(self):
        self.solSystem.runTurn()


        #self.mainPanel=frontEnd
if __name__ == '__main__':
    main()