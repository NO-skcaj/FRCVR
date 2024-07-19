#!/usr/bin/env python3

import ntcore
import time
import random



def init():
    inst1 = ntcore.NetworkTableInstance.create()
    table1 = inst1.getTable("datatable")

    
    global testPub1
    global testPub2
    global testPub3

    testPub1 = table1.getDoubleTopic("x").publish()
    testPub2 = table1.getDoubleTopic("y").publish()
    testPub3 = table1.getDoubleTopic("z").publish()

    testSub1 = table1.getDoubleTopic("x").subscribe(0)  
    testSub2 = table1.getDoubleTopic("y").subscribe(0)  
    testSub3 = table1.getDoubleTopic("z").subscribe(0)  

    inst1.startClient4("inst1")
    inst1.startClient4("inst2")
    inst1.startClient4("inst3")

    TEAM = 1919
    inst1.setServerTeam(TEAM) # where TEAM=190, 294, etc, or use inst.setServer("hostname") or similar
    inst1.setServerTeam(TEAM)
    inst1.setServerTeam(TEAM)

    inst1.startDSClient() # recommended if running on DS computer; this gets the robot IP from the DS
    inst1.startDSClient()
    inst1.startDSClient()

    testPub1.set(0)
    testPub2.set(0)
    testPub3.set(0)

    global rot

    
def send(xyz):
    x = xyz[0] 
    y = xyz[1]
    z = xyz[2]
    
    #y = 0
    #z = 0
    
    testPub1.set(x)
    testPub2.set(y)
    testPub3.set(z) 
    
    print(f"1: {x} 2: {y} 3: {z}")