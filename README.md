# ros_galapagos_cormorant
ROS package for industrial-camera autofocusing solution

## Setting NVIDIA Jetson TX2

### Install ROS & OpenCV

```bash
sudo sh -c 'echo "deb http://packages.ros.org/ros/ubuntu $(lsb_release -sc) main" > /etc/apt/sources.list.d/ros-latest.list'
sudo apt-key adv --keyserver 'hkp://keyserver.ubuntu.com:80' --recv-key C1CF6E31E6BADE8868B172B4F42ED6FBAB17C654
sudo apt update
sudo apt install ros-melodic-desktop-full
apt search ros-melodic
sudo rosdep init
rosdep update
echo "source /opt/ros/melodic/setup.bash" >> ~/.bashrc
source ~/.bashrc
sudo apt install python-rosinstall python-rosinstall-generator python-wstool build-essential
sudo apt install python3-pip
pip3 install cython  # Dependent package of numpy
pip3 install numpy   # Dependent package of opencv

printenv | grep ROS  # Check that environment variables like ROS_ROOT and ROS_PACKAGE_PATH are set.
source /opt/ros/melodic/setup.bash
mkdir -p ~/catkin_ws/src
cd ~/catkin_ws/
catkin_make
echo "source ~/catkin_ws/devel/setup.bash" >> ~/.bashrc

cd ~/catkin_ws/src
git clone https://github.com/ROBOTIS-GIT/hls_lfcd_lds_driver.git
git clone https://github.com/ROBOTIS-GIT/turtlebot3_msgs.git
git clone https://github.com/ROBOTIS-GIT/turtlebot3.git
cd ~/catkin_ws/src/turtlebot3
sudo rm -r turtlebot3_description/ turtlebot3_teleop/ turtlebot3_navigation/ turtlebot3_slam/ turtlebot3_example/
sudo apt-get install ros-melodic-rosserial-python ros-melodic-tf

sudo apt install nano  # For personal use
```


- Reboot the TX2, then

```bash
source /opt/ros/melodic/setup.bash
cd ~/catkin_ws && catkin_make -j1
rosrun turtlebot3_bringup create_udev_rules
```

### Set connection to 5G Wifi

> NOTE: In KU1006, Wifi `TB_Wifi_1_5G` is set the channel to 44, and other APs are set the channel above 144^. Therefore only `TB_Wifi_1_5G` AP is visible for TX2.

```bash
iwlist reg set US  # Set AP Country as USA
sudo refkill list
sudo reboot now
```

### Modify Codes of OpenCR

> Follow this procedure: [Manipulation - OpenCR Setup](http://emanual.robotis.com/docs/en/platform/turtlebot3/manipulation/#opencr-setup)


