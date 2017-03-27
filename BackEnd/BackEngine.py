from SolarSystem import SolarSystem
from GUI import Button
from GUI import ScreenText
from GUI import PlanetButton


class BackEngine:

    def __init__(self, backPanel):
        self.BP=backPanel
        self.turn = 0
        self.solSystem=SolarSystem(self,9)
        self.activeVessel=None

    def runTurn(self):
        self.solSystem.runTurn()

    def testFunc(self, button):
        print("Hello, from BE")
