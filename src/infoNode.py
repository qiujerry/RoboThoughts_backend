#!/usr/bin/env python
# infoNode.py
# This node subscribes to topics and posts them to the API server

import rospy
import rospkg
import yaml
from riptide_msgs.msg import ControlStatus

rpack = rospkg.RosPack()
config_path = rpack.get_path('RoboThoughts') + "backend/src/cfg/infoNode_cfg.yml"
pubs = {}
cfg = {}

def depth_callback(msg):
    depth = msg.current


def loadConfig():
    global cfg
    with open(config_path, 'r') as stream:
        cfg = yaml.load(stream)

def main():
    loadConfig()
    depth_sub = rospy.Subscriber(cfg['depth_topic'], Depth, depth_callback)

    rospy.spin()

if __name__ == "__main__":
    rospy.init_node("infoNode")
    main()