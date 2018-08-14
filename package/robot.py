#!/usr/bin/env python3
#  -*- coding: utf-8 -*-
#
# 2018-08-14
# STB
#


class Robot():

    def __init__(self, rule, color, position):
        self.color = color
        self.position = position

        self.rule = rule
        self.precedence = {col: n for n, col in enumerate(self.rule)}

        self.neighbor_left = None
        self.neighbor_right = None

    def get_neighbors(self, line):
        if self.position == len(line)-1 and self.position > 0:
            self.neighbor_left = line[self.position - 1]

        elif self.position == 0 and len(line) > 1:
            self.neighbor_right = line[self.position+1]

        elif self.position == 0 and len(line) == 1:
            pass

        else:
            self.neighbor_left = line[self.position - 1]
            self.neighbor_right = line[self.position+1]

    def move_neighbors(self, line):
        if self.neighbor_left and self.neighbor_right \
                and self.precedence[self.neighbor_left.color] > self.precedence[self.neighbor_right.color]:
            line[self.neighbor_left.position] = self.neighbor_right
            line[self.neighbor_right.position] = self.neighbor_left
            print("DO")

        self.get_neighbors(line)

        return line





