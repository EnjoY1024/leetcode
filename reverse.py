#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2020/12/3 13:07
__author__ = "hanruobing"


class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        
        str11 = str(x)
        str1 = list(str11)
        result = 0
        
        if str1[0] == '-':
            str2 = str1[1:]
            str2.reverse()
            for i in range(len(str2)):
                if str2[i] == 0:
                    str2.pop(str2[i])
                else:
                    result = int(''.join(str2))
                    # print(0-result)
            if 0 - result < -2 ** 31:
                return 0
            else:
                return 0 - result
        else:
            str1.reverse()
            for i in range(len(str1)):
                if str1[i] == 0:
                    str1.pop(str1[i])
                else:
                    result = int(''.join(str1))
            if result > 2 ** 31 - 1:
                return 0
            else:
                return result