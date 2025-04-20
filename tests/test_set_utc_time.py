"""
@file test_set_utc_time.py
@Description: This is a test script for using the SIYI SDK Python implementation to to set UTC time for the camera
@Author: Matthew, Lee
@Contact: matthew.lee@swarobo.ai
All rights reserved 2025
"""

import sys
import os
import time
from time import sleep
  
current = os.path.dirname(os.path.realpath(__file__))
parent_directory = os.path.dirname(current)
  
sys.path.append(parent_directory)

from siyi_sdk import SIYISDK

def test():
    cam = SIYISDK(server_ip="192.168.144.25", port=37260)

    if not cam.connect():
        print("No connection ")
        exit(1)

    cam.requestHardwareID() # Important to get the angles limits defined in cameras.py
    sleep(1)
    
    timestamp_us = int(time.time() * 1_000_000)
    print("Set Timestamp to", timestamp_us)
    cam.requestSetUTCTime(timestamp_us)

    sleep(1)

    print("Done and closing...")
    cam.disconnect()

if __name__ == "__main__":
    test()
