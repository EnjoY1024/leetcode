#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2020/11/24 19:20
__author__ = "hanruobing"


class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if len(strs) == 0:
            return ''

        if len(strs) == 1:
            return strs[0]

        c, minist = min([(len(s), s) for s in strs])
        #print(c,minist)
        if c == 0:
            return ''
        flag = False
        if c == 1:
            for s in strs:
                if s[0] != minist[0]:
                    flag = False
                    return ''
                else:
                    flag = True
                    continue

            if flag == True:
                return minist[0]

        flag2 = False
        for i in range(c):
            ind = minist[i]
        #print(ind)
            for s in strs:
                if s[i] != ind:
                    return s[0:i]
                else:
                    flag2 = True
                    continue

        if flag2 == True:
            return minist

s = Solution()
print(s.longestCommonPrefix(["flower","flow","flight"]))

