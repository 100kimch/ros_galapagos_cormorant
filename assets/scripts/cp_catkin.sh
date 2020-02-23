# Declare variables first before using this script:
#   export PATH_CATKIN="/your/path/to/catkin_ws"
#   export PATH_PACKAGE="/your/modified/package/path"
#   export NAME_PACKAGE="your-package-name"

echo "running to make packages"
echo ${NAME_PACKAGE}
rm -rf ${PATH_CATKIN}/src/${NAME_PACKAGE}
cp -r ${PATH_PACKAGE} ${PATH_CATKIN}/src/${NAME_PACKAGE}
cd ${PATH_PACKAGE}
sudo chmod -R 777 *
cd ${PATH_CATKIN}
catkin_make
