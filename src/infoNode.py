#!/usr/bin/env python
# infoNode.py
# This node subscribes to topics and posts them to the API server

import rospy
import rospkg
import yaml

from riptide_msgs.msg import ControlStatus
from riptide_msgs.msg import Depth
from riptide_msgs.msg import Dvl
from riptide_msgs.msg import Imu
from riptide_msgs.msg import Object
from riptide_msgs.msg import SwitchState
from darknet_ros_msgs.msg import BoundingBoxes

from std_msgs.msg import String

rpack = rospkg.RosPack()
config_path = rpack.get_path('riptide_robothoughts') + "/cfg/infoNode_cfg.yaml"
pubs = {}
cfg = {}

def controls_depth_callback(msg):
    reference = msg.reference
    current = msg.current
    error = msg.error
    f = open('data.txt', 'a+')
    f.write(reference)
    f.write(current)
    f.write(error)
    f.close()

def state_depth_callback(msg):
    depth = msg.depth
    pressure = msg.pressure
    temp = msg.temp
    altitude = msg.altitude

def bboxes_callback(msg):
    top_left = msg.top_left
    bottom_right = msg.bottom_right

def dvl_callback(msg):
    time = msg.time
    dt1 = msg.dt1
    dt2 = msg.dt2
    velocity = msg.velocity
    vehicle_pos = msg.vehicle_pos
    figure_of_merit = msg.figureOfMerit
    beam_distance = msg.beamDistance
    battery_voltage = msg.batteryVoltage
    speed_sound = msg.speedSound
    pressure = msg.pressure
    temp = msg.temp


def imu_callback(msg):
    test = 1

def object_callback(msg):
    test = 1

def switches_callback(msg):
    test = 1

def loadConfig():
    global cfg
    with open(config_path, 'r') as stream:
        cfg = yaml.load(stream)

def main():
    loadConfig()

    controls_depth_sub = rospy.Subscriber(cfg['controls_depth_topic'], ControlStatus, controls_depth_callback)
    state_depth_sub = rospy.Subscriber(cfg['state_depth_topic'], Depth, state_depth_callback)
    bboxes_sub = rospy.Subscriber(cfg['bboxes_topic'], BoundingBoxes, bboxes_callback)
    dvl_sub = rospy.Subscriber(cfg['dvl_topic'], Dvl, dvl_callback)
    imu_sub = rospy.Subscriber(cfg['imu_topic'], Imu, imu_callback)
    object_sub = rospy.Subscriber(cfg['object_topic'], Object, object_callback)
    switches_sub = rospy.Subscriber(cfg['switches_topic'], SwitchState, switches_callback)

    rospy.spin()

if __name__ == "__main__":
    rospy.init_node("infoNode")
    main()
