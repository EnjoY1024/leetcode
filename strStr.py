#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2021/2/2 22:53
__author__ = "hanruobing"


class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """

        h = len(haystack)
        n = len(needle)

        for start in range(0,h-n+1):
            if haystack[start:start+n]==needle:
                return start
        return -1

