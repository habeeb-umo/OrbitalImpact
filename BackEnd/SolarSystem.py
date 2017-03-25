from Body import Body



class SolarSystem:
    def __init__(self,backEngine):
        self.BE=backEngine
        self.name="noname"
        self.celestialList=[]

        self.celestialList.append(Body(self,1,0,"Planet 0"))
        self.celestialList.append(Body(self, 1, 1, "Planet 1"))
        self.celestialList.append(Body(self, 2, 2, "Planet 2"))
        self.celestialList.append(Body(self, 2, 3, "Planet 3"))
        self.celestialList.append(Body(self, 3, 4, "Planet 4"))

    def __str__(self):
        s=""
        for planet in self.celestialList:
            s=s+str(planet)+"\n"
        return s

    def getBody(self, index):
        return self.celestialList[index]

    def runTurn(self):
        for planet in self.celestialList:
            planet.runTurn()


