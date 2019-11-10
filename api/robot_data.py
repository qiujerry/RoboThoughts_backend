global depth
global pressure
global temp
global altitude

def state_depth_callback(msg):
    depth = msg.depth
    pressure = msg.pressure
    temp = msg.temp
    altitude = msg.altitude