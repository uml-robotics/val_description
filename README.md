#Project Name - val_description
#Maintainer - Jordan Lack - jlack1987@gmail.com

The val_description package contains the files needed to generate an URDF for Valkyrie as well as the meshes for visualization. 

#Usage Instructions
**Make sure val_description and val_description/common_xacro are in ROS_PACKAGE_PATH**
Before generating the Valkyrie URDF, you must first:

- Have ROS installed(we use ROS-Indigo)
- Add the val_description package to you ROS_PACKAGE_PATH
- Add val_description/common_xacro to your ROS_PACKAGE_PATH

Once you have done this, you can generate the URDF by:
```bash
cd <path_to_val_description>/robots/valkyrie_A
rosrun xacro xacro.py xacro/valkyrie_A.xacro -o valkyrie_A.urdf
```

After generating the URDF, you may generate an SDF file by executing the following command from the top level package directory:
```bash
gzsdf print valkyrie_A.urdf
```

You can visualize the frames in RVIZ by:
```bash
cd test
roslaunch VisualizeFramesInRviz.launch
```

To see Valkyrie in Gazebo, execute the following command from the top level package directory:
```bash
cd test
roslaunch ValkyrieInEmptyWorld.launch
```

#Credits
Johnson Space Center - ER4 - Valekryie Team

#License
NASA 1.3