#!/usr/bin/env pybricks-micropython
from pybricks.hubs import EV3Brick
from pybricks.ev3devices import (Motor, TouchSensor, ColorSensor,
                                 InfraredSensor, UltrasonicSensor, GyroSensor)
from pybricks.parameters import Port, Stop, Direction, Button, Color
from pybricks.tools import wait, StopWatch, DataLog
from pybricks.robotics import DriveBase
from pybricks.media.ev3dev import SoundFile, ImageFile


ev3 = EV3Brick()
line_sensor = ColorSensor(Port.S4)
dis_sensor= UltrasonicSensor(Port.S2)
left_motor = Motor(Port.B)
right_motor = Motor(Port.D)
robot = DriveBase(left_motor, right_motor, wheel_diameter=55.5, axle_track=104)
ev3.speaker.beep()
Line_RightSide = True
while True:
    r, g, b =  line_sensor.rgb()
    ev3.screen.print(r)
    ev3.screen.print(g)
    ev3.screen.print(b)
    ev3.screen.print(Line_RightSide)
    ev3.screen.print(dis_sensor.distance())
    wait(100)
    ev3.screen.clear()
    
    if r < 20:
        if Line_RightSide == True:
            wait(45)
            robot.drive(50, -90)
            Line_RightSide = False
        else:
            wait(45)
            robot.drive(50, 90)
            Line_RightSide = True

        
    if r > 20: 
        if Line_RightSide == True:
            robot.drive(50, 90)
        else:
            robot.drive(50, -90)
            


    if g < 20: #blue when see obstacle stop and turn back 
        if dis_sensor.distance() < 220:
            robot.stop()
            ev3.speaker.beep()
            wait(2000)
            ev3.speaker.beep()
            if Line_RightSide == True:
                robot.turn(70)
                Line_RightSide = False
            else: 
                robot.turn(70)
                Line_RightSide = True
    if g > 20 and g < 43:  #green push obstacle off tape 10cm
        if dis_sensor.distance() < 180:
            robot.stop() #turn back touchline stop based one x
            ev3.speaker.beep()
            wait(2000)
            if Line_RightSide == True:
                ev3.speaker.beep()
                robot.drive(30, 90)
                wait(300)
            else:
                ev3.speaker.beep()
                robot.drive(30,-90)
                wait(300)
            robot.drive(90, 0)
            wait(900)
            robot.turn(-100)
            robot.drive(90, 0)
            wait(1500)
            
            if Line_RightSide == True:
                robot.drive(-90, 0)
                wait(1500)
                robot.turn(100)
                robot.drive(-90, 0)
                if r < 20:
                    robot.stop()
                Line_RightSide = False
            else: 
                robot.drive(-90, 0)
                wait(1500)
                robot.turn(100)
                robot.drive(-90, 0)
                if r < 20:
                    robot.stop()
                Line_RightSide = True









#if turning left and crossline, then line has to be on the right. 
