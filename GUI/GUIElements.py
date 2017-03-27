from direct.gui.OnscreenText import OnscreenText, TextNode
from panda3d.core import NodePath


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
        self.place()

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

    def place(self):
        enode = self.panel.loader.loadModel(self.getPullLocation())
        enode.setHpr(0,0,90)
        enode.setScale(self.scale)
        self.panel.makePickable(enode)
        x = self.panel.XgridToLoc(self.x)
        y = self.panel.YgridToLoc(self.y)
        enode.setPos(-.11,x,y)
        enode.setShaderAuto()
        enode.reparentTo(self.panel.getPanelNode())
        self.panel.addToElementList([enode,self])
        self.element = enode

    def getNode(self):
        return self.element

class PlanetButton(Button):
    def __init__(self, Panel, x,y,clickFunc):
        self.pullLocation = "GDAT/Meshes/planet_sphere.egg.pz"
        Button.__init__(self,Panel,x,y,clickFunc)
        self.element.setTexture(Panel.loader.loadTexture("GDAT/Textures/hubble_friday_07012016.jpg"))
    def getPullLocation(self):
        return "GDAT/Meshes/planet_sphere.egg.pz"
    def getTextureLocation(self):
        return "GDAT/Textures/hubble_friday_07012016.jpg"

class ScreenText:
    def __init__(self, Panel, x, y, data):
        self.data=data
        self.x = x-.5
        self.y = y-.5
        self.Panel=Panel
        self.place()

    def updateText(self, text):
        data=text
        self.textObject.setText(text)

    def getText(self):
        return self.data
    def getXGrid(self):
        return self.x
    def getYGrid(self):
        return self.y

    def place(self):
        containerNode = NodePath("TextContainer")
        containerNode.reparent_to(self.Panel.getPanelNode())
        containerNode.setHpr(-90,0,0)
        x = self.Panel.XgridToLoc(self.x)
        y = self.Panel.YgridToLoc(self.y)
        containerNode.setPos(-.1000001, x, y)
        textObject =  OnscreenText(text = self.getText(), scale = 0.032, parent=containerNode)
        textObject.setAlign(TextNode.A_boxed_left)
        self.node = containerNode
        self.textObject = textObject;

    def remove(self):
        self.textObject.removeNode()
        self.node.removeNode()