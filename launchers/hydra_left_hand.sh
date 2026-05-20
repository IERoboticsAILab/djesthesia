#!/bin/bash

sleep 0.5
HOST="saeka@hydra"

ssh "$HOST" "source setting.sh && roslaunch optitrack_ros_communication optitrack_udp.launch number_of_nodes:=2 ip:=10.205.3.18 base_port:=10876"