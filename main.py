#!/usr/bin/env python3
#  -*- coding: utf-8 -*-
#
# 2018-08-14
# STB
#

from package import Robot
from package import Line


rule = ["red", "blue"]


myline = Line(rule)
myline.add_robot()
myline.display()

myline.add_robot()
myline.display()

myline.add_robot()
myline.display()

myline.add_robot()
myline.display()

myline.add_robot()
myline.display()
