import sys
import maya.OpenMaya as OpenMaya
import maya.OpenMayaMPx as OpenMayaMPx
import maya.cmds as cmds
import maya.mel as mel

kPluginCmdName = "myAddShelvesItem"

# command
class scriptedCommand(OpenMayaMPx.MPxCommand):
	def __init__(self):
		OpenMayaMPx.MPxCommand.__init__(self)
	def doIt(self,argList):
		#falg
		ifAddButton_b = True
		#Shelves Name
		myShelvesName_str = 'Anim'
		#Label made by yourself
		myShelvesItemLabel_str = "optimization display"
		#Since it is placed under Anim, it must be acquired first
		ShelvesItem = cmds.shelfLayout(myShelvesName_str, q=True, childArray=True)
		#itemButton refers to the button under the tab on Shelves
		for itemButton in ShelvesItem:
		    itemLabel = cmds.shelfButton(itemButton, q=True, label=True)
		    if itemLabel == myShelvesItemLabel_str:
		        ifAddButton_b = False
		        break
		#If the button does not exist
		if ifAddButton_b:
		    cmds.shelfButton(rpt=True, i1="ai.png", label=myShelvesItemLabel_str, parent=myShelvesName_str, ann=myShelvesItemLabel_str,stp="python", c="import maya.cmds as cmds\n\nallShapes = cmds.ls( type='geometryShape' )\ncmds.displaySmoothness(allShapes ,divisionsU=0, divisionsV=0, pointsWire=4, pointsShaded=1, polygonObject=1)\n\ncmds.setAttr('hardwareRenderingGlobals.multiSampleEnable', False)\ncmds.setAttr('hardwareRenderingGlobals.ssaoEnable', False)")

# Creator
def cmdCreator():
	return OpenMayaMPx.asMPxPtr( scriptedCommand() )
	
# Initialize the script plug-in
def initializePlugin(mobject):
	mplugin = OpenMayaMPx.MFnPlugin(mobject)
	try:
		mplugin.registerCommand( kPluginCmdName, cmdCreator )
		mel.eval("myAddShelvesItem")
	except:
		sys.stderr.write( "Failed to register command: %s\n" % kPluginCmdName )
		raise

# Uninitialize the script plug-in
def uninitializePlugin(mobject):
	mplugin = OpenMayaMPx.MFnPlugin(mobject)
	try:
		mplugin.deregisterCommand( kPluginCmdName )
	except:
		sys.stderr.write( "Failed to unregister command: %s\n" % kPluginCmdName )
		raise
