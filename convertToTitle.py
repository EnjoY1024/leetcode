#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2021/3/30 22:13
__author__ = "hanruobing"

class Solution(object):
    def convertToTitle(self, columnNumber):
        """
        :type columnNumber: int
        :rtype: str
        """
        yingshe = {'A':1,'B':2,'C':3,'D':4,'E':5,'F':6,'G':7,'H':8,'I':9,
                'J':10,'K':11,'L':12,'M':13,'N':14,'O':15,'P':16,'Q':17,
                'R':18,'S':19,'T':20,'U':21,'V':22,'W':23,'X':24,'Y':25,'Z':26}
        flag = True
        shang = []
        yu = []
        while flag:
            if columnNumber//26<26:
                flag = False
                shang = columnNumber//26
                yu = columnNumber%26
            else:
                shang =