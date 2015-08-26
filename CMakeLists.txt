cmake_minimum_required(VERSION 2.8.3)
project(val_description)

## Find catkin macros and libraries
## if COMPONENTS list like find_package(catkin REQUIRED COMPONENTS xyz)
## is used, also find other catkin packages
find_package(catkin REQUIRED COMPONENTS
  xacro 
)

set(urdf_files "")

# Xacro files
file(GLOB model_xacro_files ${CMAKE_CURRENT_SOURCE_DIR}/robots/common/*/*.xacro ${CMAKE_CURRENT_SOURCE_DIR}/robots/valkyrie_A/*/*.xacro ${CMAKE_CURRENT_SOURCE_DIR}/robots/valkyrie_B/*/*.xacro)
file(GLOB instance_xacro_files ${CMAKE_CURRENT_SOURCE_DIR}/robots/common/*/*.xacro ${CMAKE_CURRENT_SOURCE_DIR}/robots/valkyrie_A/*/*.xacro ${CMAKE_CURRENT_SOURCE_DIR}/robots/valkyrie_B/*/*.xacro)

# Robot files
file(GLOB urdf_xacro_files ${CMAKE_CURRENT_SOURCE_DIR}/robots/*.xacro)

# Create urdf dir
file(MAKE_DIRECTORY ${CMAKE_CURRENT_SOURCE_DIR}/urdf)

foreach(it ${urdf_xacro_files})
  get_filename_component(basepath ${it} PATH)
  get_filename_component(basename ${it} NAME_WE)

  message("processing urdf file :" ${basepath}/${basename})

  set(expanded_file "${CMAKE_CURRENT_SOURCE_DIR}/urdf/${basename}.urdf")
  message("produce expanded file :" ${expanded_file})

  xacro_add_xacro_file(${it} ${expanded_file})
  
  set(urdf_files ${urdf_files} ${expanded_file})
endforeach(it)

# file(GLOB xacro_files ${CMAKE_CURRENT_SOURCE_DIR}/instances/robots/xacro/*/*.xacro)

# # Robot files
# file(GLOB instance_xacro_files ${CMAKE_CURRENT_SOURCE_DIR}/instances/robots/*.xacro)

# # Create urdf dir
# file(MAKE_DIRECTORY ${CMAKE_CURRENT_SOURCE_DIR}/instances/instance_files)

# foreach(it ${instance_xacro_files})
#   get_filename_component(basepath ${it} PATH)
#   get_filename_component(basename ${it} NAME_WE)

#   message("processing xml file :" ${basepath}/${basename})

#   set(expanded_file "${CMAKE_CURRENT_SOURCE_DIR}/instances/instance_files/${basename}.xml")
#   message("produce expanded file :" ${expanded_file})

#   xacro_add_xacro_file(${it} ${expanded_file})
  
#   set(instance_files ${instance_files} ${expanded_file})
# endforeach(it)

###################################
## catkin specific configuration ##
###################################
## The catkin_package macro generates cmake config files for your package
## Declare things to be passed to dependent projects
## INCLUDE_DIRS: uncomment this if you package contains header files
## LIBRARIES: libraries you create in this project that dependent projects also need
## CATKIN_DEPENDS: catkin_packages dependent projects also need
## DEPENDS: system dependencies of this project that dependent projects also need
catkin_package(
#  INCLUDE_DIRS include
#  LIBRARIES val_description
#  CATKIN_DEPENDS xacro
#  DEPENDS system_lib
)

add_custom_target(val_description_media_files ALL DEPENDS ${urdf_files})

# install urdf and xacro files
install(DIRECTORY materials/
  DESTINATION ${CATKIN_PACKAGE_SHARE_DESTINATION}/materials
)
install(DIRECTORY meshes/
  DESTINATION ${CATKIN_PACKAGE_SHARE_DESTINATION}/meshes
)
install(DIRECTORY robots/
  DESTINATION ${CATKIN_PACKAGE_SHARE_DESTINATION}/robots
)
install(DIRECTORY urdf/
  DESTINATION ${CATKIN_PACKAGE_SHARE_DESTINATION}/urdf
)
