from GUI import ScreenText
from GUI import PlanetButton
from GUI import Button


class Vessel:
    def __init__(self, BE, name):
        self.name = name
        self.BE = BE
        self.ChoseStart()
        self.veselData=ScreenText(self.BE.getBackPanel(),15,2,"No Planet Data")

    def completeInit(self):
        self.navData = ScreenText(self.BE.getBackPanel(), 15, 7, "")
        self.targetPlanet = self.planet
        self.navPlanet = self.planet
        self.navInfButton = Button(self.BE.getBackPanel(),15,9.5,self.navInfEvent)
        self.navinfMessage = ScreenText(self.BE.getBackPanel(),15,11, "Inf")
        self.navSelButton = Button(self.BE.getBackPanel(),16,9.5,self.navSelEvent)
        self.navSelMessage = ScreenText(self.BE.getBackPanel(),16,11, "Sel")
        self.navPostButton = Button(self.BE.getBackPanel(),17,9.5,self.navPostEvent)
        self.navPostMessage = ScreenText(self.BE.getBackPanel(), 17, 11, "Pos")
        self.displayVesselInfo()
        #self.displayNavigation()

    def ChoseStart(self):
        self.message = ScreenText(self.BE.getBackPanel(),0,.5,"Select a Starting Planet")
        self.pButtons = []
        for i in range (0, len(self.BE.getSolarSystem()),1):
            self.pButtons.append(PlanetButton(self.BE.getBackPanel(),i,1,self.selectedPlanet))

    def selectedPlanet(self, buttonClicked):
        for i in range(0, len(self.pButtons), 1):
            if self.pButtons[i] == buttonClicked:
                self.clearStart(i)
                return

    def clearStart(self, planetIndex):
        self.message.remove()
        self.planet=self.BE.getSolarSystem()[planetIndex]
        for p in self.pButtons:
            p.remove()
            self.completeInit()

    def displayVesselInfo(self):

        data = "Vessel Data:\n"
        data += "Name: "+str(self.name)+"\n"
        data += "Location: "+self.planet.getName()+"\n"
        data += "Target: "+self.targetPlanet.getName()
        self.veselData.updateText(data)

    def displayNavigation(self):
        navDataText = "NAV Data\n"
        navDataText += "Selected Target: "+self.navPlanet.getName()+"\n"
        navDataText += "Dv To Target: "+str(self.planet.distanceTo(self.navPlanet))+"\n"
        self.navData.updateText(navDataText)

    def navEvent(self, button):
        print "TODO!"

    def navInfEvent(self, button):
        self.navPlanet = self.navPlanet.getInferior()
        self.displayNavigation()

    def navPostEvent(self, button):
        self.navPlanet = self.navPlanet.getPosterior()
        self.displayNavigation()

    def navSelEvent(self, button):
        self.targetPlanet = self.navPlanet
        self.displayNavigation()
        self.displayVesselInfo()

    def runTurn(self):
        self.displayVesselInfo()
        self.displayNavigation()
