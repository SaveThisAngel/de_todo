import sys
import win32api, win32con, win32process, win32gui
import time
import psutil
import math
import numpy as np

move_array = np.array([
[ -61 , 87 ],
[ 9 , 80 ],
[ -96 , 73 ],
[ -74 , 65 ],
[ 0 , 58 ],
[ 29 , 50 ],
[ 51 , 42 ],
[ 66 , 34 ],
[ 73 , 25 ],
[ 74 , 17 ],
[ 66 , 17 ],
[ 52 , 32 ],
[ 30 , 44 ],
[ 2 , 52 ],
[ -26 , 57 ],
[ -48 , 58 ],
[ -65 , 56 ],
[ -75 , 51 ],
[ -80 , 42 ],
[ -79 , 30 ],
[ -73 , 15 ],
[ -61 , 9 ],
[ -43 , 24 ],
[ -19 , 36 ],
[ 21 , 45 ],
[ 63 , 49 ],
[ 85 , 49 ],
[ 86 , 45 ],
[ 67 , 37 ]])

def right_mouse_down():
    lmb_state = win32api.GetKeyState(0x01)
    return lmb_state < 0

def left_mouse_down():    
    rmb_state = win32api.GetKeyState(0x02)
    return rmb_state < 0   

current_array = move_array

pos1 = win32api.GetCursorPos()
win32api.mouse_event(win32con.MOUSEEVENTF_MOVE,current_array[0][0],current_array[0][1])
pos2 = win32api.GetCursorPos()
mouse_pos = np.array([[pos1], [pos2]])
total_moved = (mouse_pos[1] - mouse_pos[0])
print(total_moved)