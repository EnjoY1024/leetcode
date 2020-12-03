#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2020/12/3 13:09
__author__ = "hanruobing"

class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        result  = True
        if x<0:
            result = False
        else:
            li = str(x)
            if x == int(li[::-1]):
                result = True
            else:
                result = False

        return result