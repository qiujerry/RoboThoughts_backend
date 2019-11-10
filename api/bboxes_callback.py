#creates global variables for bboxes. Each time bboxes_callback is called it updates 
#top_left and bottom_right 

global top_left
global bottom_right


def bboxes_callback(msg):
    top_left = msg.top_left
    bottom_right = msg.bottom_right