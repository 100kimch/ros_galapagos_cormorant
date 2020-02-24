# Declare variables first before using this script:
#   export PATH_CATKIN="/your/path/to/catkin_ws"
#   export PATH_PACKAGE="/your/modified/package/path"
#   export NAME_PACKAGE="your-package-name"
#   export PYTHON_VER="3.5"

echo "running to make packages"
echo ${NAME_PACKAGE}
rm -rf ${PATH_CATKIN}/src/${NAME_PACKAGE}
cp -r ${PATH_PACKAGE} ${PATH_CATKIN}/src/${NAME_PACKAGE}
cd ${PATH_PACKAGE}
sudo chmod -R 777 *
cd ${PATH_CATKIN}
sudo apt-get install python3-pip python3-yaml
sudo pip3 install rospkg catkin_pkg
sudo apt-get install python-catkin-tools python3-dev python3-numpy
catkin config -DPYTHON_EXECUTABLE=/usr/bin/python3 -DPYTHON_INCLUDE_DIR=/usr/include/python${PYTHON_VER}m -DPYTHON_LIBRARY=/usr/lib/x86_64-linux-gnu/libpython${PYTHON_VER}m.so
catkin config --install
cd src
git clone -b kinetic https://github.com/ros-perception/vision_opencv
cd ..
catkin build cv_bridge
source install/setup.bash --extend
cd ~
