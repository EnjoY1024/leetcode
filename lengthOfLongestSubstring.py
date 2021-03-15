#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2021/3/15 22:07
__author__ = "hanruobing"


class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        n = len(s)

        if n == 0:
            return 0

        for i in range(n-1,0,-1):
            for ind in range(0,n-i+2):
                if len(s[ind:ind+i]) == len(set(s[ind:ind+i])):
                    return s[ind:ind+i]

s = Solution()
print(s.lengthOfLongestSubstring("aab"))

#超时