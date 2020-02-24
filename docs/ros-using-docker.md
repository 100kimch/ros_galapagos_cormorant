# ROS using docker

- author: Kim Jihyeong (kjhricky@gmail.com)
- written in 2020. Feb. 11.

## Overview

This tutorial provides information how to set up ros system using docker.

## Steps

### Install docker

See other document:

### Install ROS

```bash
docker pull ros:latest
docker ps
docker run -i -t --net="host" --privileged test_ros:version2 /bin/bash
```

- In the `ros` docker container:

```bash
apt install nano iputils-ping net-tools traceroute -y
ping www.google.com
```

- When ping is responded, the container connects internet successfully.

```bash
nano ~/.bashrc
```

- In the `~/.bashrc`:

```text
source /opt/ros/melodic/setup.bash
source ~/catkin_ws/devel/setup.bash

export ROS_MASTER_URI=http://192.168.1.206:11311
export ROS_HOSTNAME=192.168.1.204
export TURTLEBOT3_MODEL=waffle_pi
```
