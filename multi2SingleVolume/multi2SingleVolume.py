import os
import unittest
from __main__ import vtk, qt, ctk, slicer
from slicer.ScriptedLoadableModule import *

#
# multi2SingleVolume
#

class multi2SingleVolume(ScriptedLoadableModule):
  """Uses ScriptedLoadableModule base class, available at:
  https://github.com/Slicer/Slicer/blob/master/Base/Python/slicer/ScriptedLoadableModule.py
  """

  def __init__(self, parent):
    ScriptedLoadableModule.__init__(self, parent)
    self.parent.title = "multi2SingleVolume" # TODO make this more human readable by adding spaces
    self.parent.categories = ["Gatti"]
    self.parent.dependencies = []
    self.parent.contributors = ["Anthony Gatti (McMaster)"] # replace with "Firstname Lastname (Organization)"
    self.parent.helpText = """
    This is an example of scripted loadable module bundled in an extension.
    """
    self.parent.acknowledgementText = """
    This file was originally developed by Jean-Christophe Fillion-Robin, Kitware Inc.
    and Steve Pieper, Isomics, Inc. and was partially funded by NIH grant 3P41RR013218-12S1.
""" # replace with organization, grant and thanks.

#
# multi2SingleVolumeWidget
#

class multi2SingleVolumeWidget(ScriptedLoadableModuleWidget):
  """Uses ScriptedLoadableModuleWidget base class, available at:
  https://github.com/Slicer/Slicer/blob/master/Base/Python/slicer/ScriptedLoadableModule.py
  """

  def setup(self):
    ScriptedLoadableModuleWidget.setup(self)
    # Instantiate and connect widgets ...

    #
    # Parameters Area
    #
    parametersCollapsibleButton = ctk.ctkCollapsibleButton()
    parametersCollapsibleButton.text = "Parameters"
    self.layout.addWidget(parametersCollapsibleButton)

    # Layout within the dummy collapsible button
    parametersFormLayout = qt.QFormLayout(parametersCollapsibleButton)

    #
    # input volume selector
    #
    self.inputSelector = slicer.qMRMLNodeComboBox()
    self.inputSelector.nodeTypes = ( ("vtkMRMLMultiVolumeNode"), "" )
    # self.inputSelector.addAttribute( "vtkMRMLScalarVolumeNode", "LabelMap", 0 )
    self.inputSelector.selectNodeUponCreation = True
    self.inputSelector.addEnabled = False
    self.inputSelector.removeEnabled = False
    self.inputSelector.noneEnabled = False
    self.inputSelector.showHidden = False
    self.inputSelector.showChildNodeTypes = False
    self.inputSelector.setMRMLScene( slicer.mrmlScene )
    self.inputSelector.setToolTip( "Pick the input to the algorithm." )
    parametersFormLayout.addRow("Input Volume: ", self.inputSelector)

    #
    # output volume selector
    #
    self.outputSelector = slicer.qMRMLNodeComboBox()
    self.outputSelector.nodeTypes = ( ("vtkMRMLScalarVolumeNode"), "" )
    # self.outputSelector.addAttribute( "vtkMRMLScalarVolumeNode", "LabelMap", 0 )
    self.outputSelector.selectNodeUponCreation = True
    self.outputSelector.addEnabled = True
    self.outputSelector.removeEnabled = True
    self.outputSelector.noneEnabled = True
    self.outputSelector.showHidden = False
    self.outputSelector.showChildNodeTypes = False
    self.outputSelector.setMRMLScene( slicer.mrmlScene )
    self.outputSelector.setToolTip( "Pick the output to the algorithm." )
    parametersFormLayout.addRow("Output Volume: ", self.outputSelector)

    #
    # Apply Button
    #
    self.applyButton = qt.QPushButton("Apply")
    self.applyButton.toolTip = "Run the algorithm."
    self.applyButton.enabled = False
    parametersFormLayout.addRow(self.applyButton)

    # connections
    self.applyButton.connect('clicked(bool)', self.onApplyButton)
    self.inputSelector.connect("currentNodeChanged(vtkMRMLNode*)", self.onSelect)
    self.outputSelector.connect("currentNodeChanged(vtkMRMLNode*)", self.onSelect)

    # Add vertical spacer
    self.layout.addStretch(1)

  def cleanup(self):
    pass

  def onSelect(self):
    self.applyButton.enabled = self.inputSelector.currentNode() and self.outputSelector.currentNode()

  def onApplyButton(self):
    # logic = multi2SingleVolumeLogic()
 #    print("Run the algorithm")
 #    logic.run(self.inputSelector.currentNode(), self.outputSelector.currentNode(), enableScreenshotsFlag,screenshotScaleFactor)
     inputVolume = self.inputSelector.currentNode()
     outputVolume = self.outputSelector.currentNode()
     
     


##
# # multi2SingleVolumeLogic
# #
#
# class multi2SingleVolumeLogic(ScriptedLoadableModuleLogic):
#   """This class should implement all the actual
#   computation done by your module.  The interface
#   should be such that other python code can import
#   this class and make use of the functionality without
#   requiring an instance of the Widget.
#   Uses ScriptedLoadableModuleLogic base class, available at:
#   https://github.com/Slicer/Slicer/blob/master/Base/Python/slicer/ScriptedLoadableModule.py
#   """
#
#   def hasImageData(self,volumeNode):
#     """This is a dummy logic method that
#     returns true if the passed in volume
#     node has valid image data
#     """
#     if not volumeNode:
#       print('no volume node')
#       return False
#     if volumeNode.GetImageData() == None:
#       print('no image data')
#       return False
#     return True
#
#   def takeScreenshot(self,name,description,type=-1):
#     # show the message even if not taking a screen shot
#     self.delayDisplay(description)
#
#     if self.enableScreenshots == 0:
#       return
#
#     lm = slicer.app.layoutManager()
#     # switch on the type to get the requested window
#     widget = 0
#     if type == slicer.qMRMLScreenShotDialog.FullLayout:
#       # full layout
#       widget = lm.viewport()
#     elif type == slicer.qMRMLScreenShotDialog.ThreeD:
#       # just the 3D window
#       widget = lm.threeDWidget(0).threeDView()
#     elif type == slicer.qMRMLScreenShotDialog.Red:
#       # red slice window
#       widget = lm.sliceWidget("Red")
#     elif type == slicer.qMRMLScreenShotDialog.Yellow:
#       # yellow slice window
#       widget = lm.sliceWidget("Yellow")
#     elif type == slicer.qMRMLScreenShotDialog.Green:
#       # green slice window
#       widget = lm.sliceWidget("Green")
#     else:
#       # default to using the full window
#       widget = slicer.util.mainWindow()
#       # reset the type so that the node is set correctly
#       type = slicer.qMRMLScreenShotDialog.FullLayout
#
#     # grab and convert to vtk image data
#     qpixMap = qt.QPixmap().grabWidget(widget)
#     qimage = qpixMap.toImage()
#     imageData = vtk.vtkImageData()
#     slicer.qMRMLUtils().qImageToVtkImageData(qimage,imageData)
#
#     annotationLogic = slicer.modules.annotations.logic()
#     annotationLogic.CreateSnapShot(name, description, type, self.screenshotScaleFactor, imageData)
#
#   def run(self,inputVolume,outputVolume,enableScreenshots=0,screenshotScaleFactor=1):
#     """
#     Run the actual algorithm
#     """
#
#     self.delayDisplay('Running the aglorithm')
#
#     self.enableScreenshots = enableScreenshots
#     self.screenshotScaleFactor = screenshotScaleFactor
#
#     self.takeScreenshot('multi2SingleVolume-Start','Start',-1)
#
#     return True
#
#
# class multi2SingleVolumeTest(ScriptedLoadableModuleTest):
#   """
#   This is the test case for your scripted module.
#   Uses ScriptedLoadableModuleTest base class, available at:
#   https://github.com/Slicer/Slicer/blob/master/Base/Python/slicer/ScriptedLoadableModule.py
#   """
#
#   def setUp(self):
#     """ Do whatever is needed to reset the state - typically a scene clear will be enough.
#     """
#     slicer.mrmlScene.Clear(0)
#
#   def runTest(self):
#     """Run as few or as many tests as needed here.
#     """
#     self.setUp()
#     self.test_multi2SingleVolume1()
#
#   def test_multi2SingleVolume1(self):
#     """ Ideally you should have several levels of tests.  At the lowest level
#     tests sould exercise the functionality of the logic with different inputs
#     (both valid and invalid).  At higher levels your tests should emulate the
#     way the user would interact with your code and confirm that it still works
#     the way you intended.
#     One of the most important features of the tests is that it should alert other
#     developers when their changes will have an impact on the behavior of your
#     module.  For example, if a developer removes a feature that you depend on,
#     your test should break so they know that the feature is needed.
#     """
#
#     self.delayDisplay("Starting the test")
#     #
#     # first, get some data
#     #
#     import urllib
#     downloads = (
#         ('http://slicer.kitware.com/midas3/download?items=5767', 'FA.nrrd', slicer.util.loadVolume),
#         )
#
#     for url,name,loader in downloads:
#       filePath = slicer.app.temporaryPath + '/' + name
#       if not os.path.exists(filePath) or os.stat(filePath).st_size == 0:
#         print('Requesting download %s from %s...\n' % (name, url))
#         urllib.urlretrieve(url, filePath)
#       if loader:
#         print('Loading %s...\n' % (name,))
#         loader(filePath)
#     self.delayDisplay('Finished with download and loading\n')
#
#     volumeNode = slicer.util.getNode(pattern="FA")
#     logic = multi2SingleVolumeLogic()
#     self.assertTrue( logic.hasImageData(volumeNode) )
#     self.delayDisplay('Test passed!')
