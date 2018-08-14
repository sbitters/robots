#!/usr/bin/env python3
#  -*- coding: utf-8 -*-
#
# 2018-08-14
# STB
#

from random import randint

from package import Robot


class Line():

    def __init__(self, rule):
        self.line = []
        self.rule = rule

    def add_robot(self):
        for robot in self.line:
            robot.position += 1

        next_color = self.rule[randint(0, len(self.rule)-1)]
        self.line = [Robot(self.rule, next_color, 0)] + self.line

        print(next_color)

        if len(self.line) > 1:
            for robot in self.line:
                robot.get_neighbors(self.line)
                self.line = robot.move_neighbors(self.line)

    def display(self):
        if self.line:
            for index, robot in enumerate(self.line):
                if index == len(self.line)-1:
                    end = ""
                else:
                    end = " - "

                print(robot.color, end=end)

        else:
            print("None")

        print("\n{}".format(self.rule))