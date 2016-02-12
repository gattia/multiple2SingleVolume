cmake_minimum_required(VERSION 2.8.9)

project(Multi2SingleVolume)

#-----------------------------------------------------------------------------
# Extension meta-information
set(EXTENSION_HOMEPAGE "http://www.example.com/Slicer/Extensions/Multi2SingleVolume")
set(EXTENSION_CATEGORY "Examples")
set(EXTENSION_CONTRIBUTORS "Anthony (McMaster)")
set(EXTENSION_DESCRIPTION "This is an example of a simple extension")
set(EXTENSION_ICONURL "http://www.example.com/Slicer/Extensions/Multi2SingleVolume.png")
set(EXTENSION_SCREENSHOTURLS "http://www.example.com/Slicer/Extensions/Multi2SingleVolume/Screenshots/1.png")

#-----------------------------------------------------------------------------
# Extension dependencies
find_package(Slicer REQUIRED)
include(${Slicer_USE_FILE})

#-----------------------------------------------------------------------------
# Extension modules
add_subdirectory(multi2SingleVolume)
## NEXT_MODULE

#-----------------------------------------------------------------------------
include(${Slicer_EXTENSION_CPACK})
