# Make sure valkyrie_description and valkyrie_description/common_xacro are in ROS_PACKAGE_PATH

# Generate URDF
cd valkyrie_description/robots/valkyrie_A
rosrun xacro xacro.py xacro/valkyrie_A.xacro -o valkyrie_A.urdf

# Generate SDF
gzsdf print valkyrie_A.urdf

# Check out the frames in Rviz by running the following command and setting /map to Pelvis
cd test
roslaunch VisualizeFramesInRviz.launch

# Check out Valkyrie in Gazebo
cd test
roslaunch ValkyrieInEmptyWorld.launch