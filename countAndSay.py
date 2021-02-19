#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2021/2/8 22:06
__author__ = "hanruobing"

class Solution(object):
    def countAndSay(self, n):
        """
        :type n: int
        :rtype: str
        """
        if n == 1:
            return '1'
        else:
            key = self.countAndSay(n-1)+'@'
            #print(key,type(key),len(key),type(len(key)))
            r = ''
            j = 0
            num = 0
            for i in range(len(key)):
                if key[j] == key[i]:
                    num +=1
                elif key[i] == '@':#如果访问到最后一个可能和前面的数字相同，为了终止，但是好像没用
                    r += str(num)
                    r += str(key[i-1])
                    break
                else:
                    r += str(num)
                    #print(key[i-1])
                    r += str(key[i-1])
                    j = i
                    num = 1
            return str(r)

s = Solution()
#s.countAndSay(2)
print(s.countAndSay(5))