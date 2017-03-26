class Button:
    #This class models a button in game, storing the location, the function to call on click, and the
    def __init__(self, Panel, x, y, clickFunc):
        #this will have to be replaced with the location an actor from the mesh of a button
        self.pullLocation = "GDAT/Meshes/Button.egg"
        self.x = x
        self.y = y
        self.scale=.023
        self.clickFunc=clickFunc
        self.panel=Panel
        self.element = self.panel.placeButton(self)

    def getPullLocation(self):
        return self.pullLocation

    def getScale(self):
        return self.scale

    def getXGrid(self):
        return self.x

    def getYGrid(self):
        return self.y

    def wasClicked(self):
        if self.clickFunc != False:
            self.clickFunc(self)

    def remove(self):
        self.element.removeNode()

class PlanetButton(Button):
    def __init__(self, Panel, x,y,clickFunc):
        Button.__init__(self,Panel,x,y,clickFunc)
        self.element.setTexture(Panel.loader.loadTexture("GDAT/Textures/hubble_friday_07012016.jpg"))
    def getPullLocation(self):
        return "GDAT/Meshes/planet_sphere.egg.pz"
    def getTextureLocation(self):
        return "GDAT/Textures/hubble_friday_07012016.jpg"


class ScreenText:
    def __init__(self, Panel, x, y, w, h, data):
        self.data=data
        self.x = x
        self.y = y
        self.w = w
        self.h = h
        self.Panel=Panel
        nodeText = Panel.placeText(self)
        self.node = nodeText[0]
        self.textObject = nodeText[1]

    def updateText(self, text):
        data=text
        self.textObject.setText(text)

    def getText(self):
        return self.data
    def getXGrid(self):
        return self.x
    def getYGrid(self):
        return self.y

    def remove(self):
        self.textObject.removeNode()
        self.node.removeNode()