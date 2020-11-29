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
        dic = {}
        min_val = ""
        # print(strs)
        for s in strs:
            dic[s] = len(s)
        # print(dic)
        min_long = min(dic.values())
        # print(min_long)
        for k, v in dic.items():
            if v == min_long:
                break
        min_val = k

        flag = True
        temp = min_val
        for s in strs:
            if temp not in s:
                flag = False
                break
            else:
                continue
        if flag == True:
            return temp
        else:
            i = -1
            for ss in strs:
                if min_val[:i] in ss:
                    continue
                else:
                    i -= 1
                    if i <= -len(min_val):
                        return ''
                    else:
                        continue
                return min_val[:i]


s = Solution()
print(s.longestCommonPrefix(["flower", "flow", "flight"]))

