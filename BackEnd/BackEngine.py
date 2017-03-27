from SolarSystem import SolarSystem
from Vessel import Vessel
from GUI import Button
from GUI import ScreenText
from GUI import PlanetButton


class BackEngine:

    def __init__(self, backPanel):
        self.BP = backPanel
        self.turn = 0
        self.solSystem = SolarSystem(self,9)
        self.activeVessel = Vessel(self, "Endurance")
        ScreenText(self.BP,41,0,"Next\nTurn")
        self.turnButton = Button(self.BP,41,1,self.runTurn)

    def runTurn(self, turnButton):
        self.solSystem.runTurn()
        self.activeVessel.runTurn()
    def getSolarSystem(self):
        return self.solSystem
    def getBackPanel(self):
        return self.BP
