#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2020/12/3 13:11
__author__ = "hanruobing"


class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        find_two = {'IV': 4, 'IX': 9, 'XL': 40, 'XC': 90, 'CD': 400, 'CM': 900}
        find_one = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
        sum = 0
        i = 0
        if len(s) <= 1:
            r = find_one.get(s)
        else:
            while 1:
                # print(s[i]+s[i+1],type(s[i]+s[i+1]))
                # print(len(s))
                if i + 1 < len(s):
                    if s[i] + s[i + 1] in find_two:
                        sum = sum + find_two.get(s[i] + s[i + 1])
                        if i + 2 >= len(s):
                            break
                        i += 2
                    else:
                        sum = sum + find_one.get(s[i])
                        if i + 1 >= len(s):
                            break
                        i += 1
                else:
                    sum = sum + find_one.get(s[i])
                    break
            
            r = sum
        return r