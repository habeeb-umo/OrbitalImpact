from direct.gui.OnscreenText import OnscreenText
from direct.showbase.ShowBase import  ShowBase
from panda3d.core import *
from pandac.PandaModules import *
from direct.interval.IntervalGlobal import *
from direct.showbase.DirectObject import DirectObject
import sys
from BackEnd import BackEngine

#Grids go from (0,0) at (1.23,.67) to (42,23) at(-1.26,-.71) with a grid width of .06


class MainPanel (ShowBase):
    def __init__(self):
        self.STEP=.06
        self.TOP=.67
        self.LEFT=1.23

        loadPrcFileData("","window-title Orbital Impact")
        loadPrcFileData("", "fullscreen 0")
        loadPrcFileData("", "win-size 1280 720")
        ShowBase.__init__(self)

        self.elementList=[] #a list of lists containing the GUI element and it's Panda3d node
        self.setUpCamNode()
        self.loadPanel()
        self.setupLights()
        self.BE=BackEngine(self)

    def setUpCamNode(self):
        self.cam.setPos(0,-27,0)
        self.cam.setHpr(0,0,0)
        self.picker= CollisionTraverser()
        self.queue = CollisionHandlerQueue()

        self.pickerNode = CollisionNode('mouseRay')
        self.pickerNP = self.cam.attachNewNode(self.pickerNode)

        self.pickerNode.setFromCollideMask(GeomNode.getDefaultCollideMask())

        self.pickerRay = CollisionRay()

        self.pickerNode.addSolid(self.pickerRay)

        self.picker.addCollider(self.pickerNP, self.queue)

        # this holds the object that has been picked
        self.pickedObj = None

        self.accept('mouse1', self.onClick)

    def loadPanel(self):
        self.render.setShaderAuto()
        #Load the back panel that all elements will be attached to
        self.backPanel = self.loader.loadModel("GDAT/Meshes/BackPanel.egg")

        self.backPanel.setPos(0,1,0)
        self.backPanel.setScale(10)
        self.backPanel.setHpr(90,0,0)
        self.backPanel.reparentTo(self.render)
        self.backPanel.setShaderAuto()
        #load the sky_box This shouldn't ever be visible, but if it is, we mainain emersion
        self.skyBox = self.loader.loadModel("GDAT/Meshes/solar_sky_sphere.egg.pz")
        self.skyBox.reparentTo(self.render)
        self.skyBox.setScale(100)

        self.skyTexture = self.loader.loadTexture("GDAT/Textures/img2.jpg")#use img 2 or img3
        self.skyBox.setTexture(self.skyTexture,1)

        #self.grid()

    def setupLights(self):
        self.primaryLightHolder=self.loader.loadModel("GDAT/Meshes/planet_sphere.egg.pz")
        self.primaryLightHolder.setPos(0,-70,50)
        self.primaryLightHolder.setScale(1)
        self.primaryLightHolder.reparentTo(self.render)

        #load the light itself
        self.mLight = Spotlight("Light")
        self.mLight.setShadowCaster(True)
        lens = PerspectiveLens()
        self.mLight.setLens(lens)
        self.mLightPointer=self.primaryLightHolder.attachNewNode(self.mLight)
        self.mLightPointer.lookAt(self.backPanel)
        self.render.setLight(self.mLightPointer)


    def grid(self):
        step = .06
        for t in range(0,42):
            tNode=self.loader.loadModel("GDAT/Meshes/planet_sphere.egg.pz")
            tNode.setTexture(self.loader.loadTexture("GDAT/Textures/hubble_friday_07012016.jpg"))
            tNode.setScale(.03)
            x=1.23-(t*step)
            y=.67
            tNode.reparentTo(self.backPanel)
            tNode.setPos(-.13,x,y)
            tNode.setShaderAuto()

        for v in range (0,23):
            tNode = self.loader.loadModel("GDAT/Meshes/planet_sphere.egg.pz")
            tNode.setTexture(self.loader.loadTexture("GDAT/Textures/hubble_friday_07012016.jpg"))
            tNode.setScale(.03)
            x = 1.23
            y = .67-(v*step)
            tNode.reparentTo(self.backPanel)
            tNode.setPos(-.13, x, y)
            tNode.setShaderAuto()


    def place(self, element):
        func = element.testFunc()
        func(element)


    def getObjectHit(self, mpos):  # mpos is the position of the mouse on the screen
        self.pickedObj = None  # be sure to reset this
        self.pickerRay.setFromLens(self.camNode, mpos.getX(), mpos.getY())
        self.picker.traverse(self.render)
        if self.queue.getNumEntries() > 0:
            self.queue.sortEntries()
            self.pickedObj = self.queue.getEntry(0).getIntoNodePath()

            parent = self.pickedObj.getParent()
            self.pickedObj = None

            while parent != self.render:
                if parent.getTag('pickable') == 'true':
                    self.pickedObj = parent
                    return parent
                else:
                    parent = parent.getParent()
        return None

    def makePickable(self, obj):
        obj.setTag('pickable', 'true')

    def onClick(self):
        self.getObjectHit(self.mouseWatcherNode.getMouse())
        if self.pickedObj != None:
            self.handleEvent(self.pickedObj)

    def handleEvent(self, picked):
        for couple in self.elementList:#find the node that was clicked in the list of elements
            if couple[0] == picked:#once found call the elements onClickFunc
                couple[1].wasClicked()
        return

    def XgridToLoc(self, xgrid):
        return self.LEFT-(xgrid*self.STEP)

    def YgridToLoc(self, ygrid):
        return self.TOP-(ygrid*self.STEP)

#-----------------------------------GUI Element Place Methods here----------------------------#
    def placeButton(self, button):
        enode = self.loader.loadModel(button.getPullLocation())
        enode.setHpr(0,0,90)
        enode.setScale(button.getScale())
        self.makePickable(enode)
        x = self.XgridToLoc(button.getXGrid());
        y = self.YgridToLoc(button.getYGrid())
        enode.setPos(-.11, x, y)
        enode.setShaderAuto()
        enode.reparentTo(self.backPanel)
        self.elementList.append([enode, button])
        return enode

    def placeText(self, element):
        #create text node
        containerNode =  NodePath("Text container")
        containerNode.reparent_to(self.backPanel)
        containerNode.setHpr(-90,0,0)
        x = self.XgridToLoc(element.getXGrid());
        y = self.YgridToLoc(element.getYGrid())
        containerNode.setPos(-.10001,x,y)
        textObject =  OnscreenText(text = element.getText(), scale = 0.032, parent=containerNode)
        self.elementList.append([containerNode, element])
        return [containerNode, textObject]

app=MainPanel()
app.run()