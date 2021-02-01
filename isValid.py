#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2020/12/3 21:37
__author__ = "hanruobing"

class Solution(object):
    #先判断字符串个数是否成对
    def isValid(self, s):
        if len(s) % 2 == 1:
            return False

        pairs = {
            ")": "(",
            "]": "[",
            "}": "{",
        }
        stack = []#用来存放左括号
        print(not stack)
        for ch in s:
            if ch in pairs.keys():#如果遍历到右括号，判断存放左括号的最新值是否与其匹配
                if not stack or stack[-1] != pairs[ch]:
                    return False
                stack.pop()
            else:#如果遍历到左括号存起来
                stack.append(ch)

        return not stack


s = Solution()
s.isValid("[C])")