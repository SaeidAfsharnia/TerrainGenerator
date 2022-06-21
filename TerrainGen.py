#####   All rights reserved for Saeid Afsharnia    #####


import maya.cmds as cmds
from random import uniform as rand

#providing initial defults for range variables
RIValueX=0.0
RIValueZ=0.0
RIValueH=0.0
RIValueD=0.0
FreqInd=0
ComponentType=0

#let create a window for UI
if cmds.window("WinTerrain",exists=True):
    cmds.deleteUI("WinTerrain")

DeformWin=cmds.window("WinTerrain",t="terrain generator",w=450,h=250)
cmds.columnLayout()
cmds.text("please provide the range you desire")
RIUserX=cmds.floatSliderGrp(l="Range for X",f=True,min=0,max=10,v=0,cc="RIValueX=cmds.floatSliderGrp(RIUserX,q=True,v=True)")
RIUserZ=cmds.floatSliderGrp(l="Range for Z",f=True,min=0,max=10,v=0,cc="RIValueZ=cmds.floatSliderGrp(RIUserZ,q=True,v=True)")
RIUserH=cmds.floatSliderGrp(l="Range for H",f=True,min=0,max=10,v=0,cc="RIValueH=cmds.floatSliderGrp(RIUserH,q=True,v=True)")
RIUserD=cmds.floatSliderGrp(l="Range for D",f=True,min=-10,max=0,v=0,cc="RIValueD=cmds.floatSliderGrp(RIUserD,q=True,v=True)")
cmds.separator(w=450)
cmds.text("please indicate the frequency of noise. higher the number, bigger the area")
FreqUser=cmds.intSliderGrp(l="Frequency Indicator",f=True,min=0,max=500,v=50,cc="FreqInd=cmds.intSliderGrp(FreqUser,q=True,v=True)")
cmds.separator(w=450)
cmds.text("choose based on what component you like to deform")
cmds.radioCollection()
cmds.radioButton(l="Vertix",cc="ComponentType=0",sl=True)
cmds.radioButton(l="Edges",cc="ComponentType=1")
cmds.radioButton(l="Faces",cc="ComponentType=2")
cmds.radioButton(l="Selection",cc="ComponentType=4")
cmds.separator(w=450)
cmds.button(l="Deform",w=100,h=50,c="DeformOBJ()")
cmds.showWindow()


#start of functions
def DeformOBJ():
    #here we identify the component type based on ComponentType value
    if ComponentType==0:
        cmds.ConvertSelectionToVertices()
        AllComp=cmds.ls(sl=True,fl=True)
    
    elif ComponentType==1:
        cmds.ConvertSelectionToEdges()
        AllComp=cmds.ls(sl=True,fl=True)
    elif ComponentType==2:
        cmds.ConvertSelectionToFaces()
        AllComp=cmds.ls(sl=True,fl=True)
    else:
        AllComp=cmds.ls(sl=True,fl=True)
    
    print (AllComp)
    
    #at this point we are just deforming son
    for i in range (0,len(AllComp),FreqInd):
        cmds.select(cl=True)
        singleComp=AllComp[i]
        cmds.select(singleComp)
        RandX=rand(-RIValueX,RIValueX)
        RandZ=rand(-RIValueZ,RIValueZ)
        RandY=rand(RIValueD,RIValueH)
        cmds.move(RandX,RandY,RandZ,r=True)













