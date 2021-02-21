#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2021/2/21 22:54
__author__ = "hanruobing"

class Solution(object):
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        len_a = len(a)
        len_b = len(b)

        if len_a>len_b:
            long = a
            short = b
        else:
            long = b
            short = a

        len_short = len(short)
        len_long = len(long)
        jinwei = 0
        r1 = '0'*len_short
        for i,j in zip(range(len_short-1,-1,-1), range(len_long-1,-1,len_long-len_short+1)):
            if carry+int(short[i])+int(long[j]) == 0:
                r1[i] = '0'
                jinwei=0
            elif carry+int(short[i])+int(long[j]) == 1:
                r1[i] = '1'
                jinwei=0
            else:
                r1[i]= '0'
                jinwei = 1
        print(r1)
        r2='0'*(len_long-len_short)
        if jinwei == 0:
            rr = long[0:len_long-len_short-1] + r1
            return rr
        else:
            for i in range(len_long-len_short-1,-1,-1):
                if jinwei+int(long[i])==2:
                    jinwei = 1
                    r2[i] = '0'
                else:
                    return long[0:len_long-len_short-1] + r1
            print(r2)
            return r2+r1


s = Solution()
print(s.addBinary('110','1'))




