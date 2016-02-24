mvNode = slicer.util.getNode('T2MAP*')
mvData = mvNode.GetImageData()

imageDimensions = mvNode.GetImageData().GetDimensions()
imageSpacing = mvNode.GetImageData().GetSpacing()

extract = vtk.vtkImageExtractComponents()
extract.SetInputData(mvData)
extract.SetComponents(0)
extract.Update()

scalarVolumeNode = slicer.vtkMRMLScalarVolumeNode()
scalarVolumeNode.SetScene(slicer.mrmlScene)
slicer.mrmlScene.AddNode(scalarVolumeNode)

ras2ijk = vtk.vtkMatrix4x4()
ijk2ras = vtk.vtkMatrix4x4()

mvNode.GetRASToIJKMatrix(ras2ijk)
mvNode.GetIJKToRASMatrix(ijk2ras)
scalarVolumeNode.SetRASToIJKMatrix(ras2ijk)
scalarVolumeNode.SetIJKToRASMatrix(ijk2ras)

scalarVolumeNode.SetAndObserveImageData(extract.GetOutput())
displayNode = scalarVolumeNode.GetDisplayNode()

scalarVolumeNode.SetName('singleVolume')