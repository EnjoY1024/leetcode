#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2021/2/19 22:10
__author__ = "hanruobing"

class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        if len(s)==0:
            return 0
        s = s.strip(' ')
        slist = s.split(' ')


        last_word = slist[-1]
        return len(last_word)

s = Solution()
print(s.lengthOfLastWord('hee   aa'))