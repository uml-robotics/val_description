# Make sure valkyrie_description is in ROS_PACKAGE_PATH

# Generate URDF
cd valkyrie_description/robots/valkyrie_A
rosrun xacro xacro.py xacro/valkyrie_A.xacro -o valkyrie_A.urdf

# Generate SDF
gzsdf print valkyrie_A.urdf
