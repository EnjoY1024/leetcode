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
        L, n = len(needle), len(haystack)

        for start in range(n - L + 1):
            if haystack[start: start + L] == needle:
                return start
        return -1
                 
s = Solution()
print(s.strStr('abc','c'))
                
