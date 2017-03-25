class Button:
    #This class models a button in game, storing the location, the function to call on click, and the
    def __init__(self, Panel, x, y, clickFunc):
        #this will have to be replaced with the location an actor from the mesh of a button
        self.pullLocation = "GDAT/Meshes/Button.egg"
        self.textureLocation="GDAT/Textures/hubble_friday_07012016.jpg"
        self.x = x
        self.y = y
        self.scale=.03
        self.clickFunc=clickFunc
        self.panel=Panel
        self.panel.placeButton(self)

    def getPullLocation(self):
        return self.pullLocation

    def testFunc(self):
        return self.panel.placeButton

    def getScale(self):
        return self.scale

    def getTextureLocation(self):
        return self.textureLocation

    def getXGrid(self):
        return self.x

    def getYGrid(self):
        return self.y

    def wasClicked(self):
        if self.clickFunc != False:
            self.clickFunc()

class ScreenText:
    def __init__(self, Panel, x, y, w, h, data):
        self.data=data
        self.x = x
        self.y = y
        self.w = w
        self.h = h
        self.Panel=Panel
        self.Panel.placeText(self)
    def getText(self):
        return self.data
    def getXGrid(self):
        return self.x
    def getYGrid(self):
        return self.y