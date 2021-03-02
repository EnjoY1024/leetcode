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

        if len_a > len_b:
            long = a
            short = b
        else:
            long = b
            short = a
        r = []
        if len_a == len_b:
            jinwei = 0
            for i in range(-1,-len_a-1,-1):
                if jinwei + int(short[i])+int(long[i]) == 0:
                    jinwei = 0
                    r.append('0')
                elif jinwei + int(short[i])+int(long[i]) == 1:
                    jinwei = 0
                    r.append('1')
                elif jinwei + int(short[i])+int(long[i]) == 2:
                    jinwei = 1
                    r.append('0')
                else:
                    jinwei = 1
                    r.append('1')
            r.reverse()
            if jinwei == 1:
                return '1'+''.join(r)
            else:
                return ''.join(r)

        jinwei = 0

        r1 = [] #将后面结果添加到列表
        #先计算short对齐的几位
        #print(list(range(-1,-len(short)-1,-1)))
        for i in range(-1,-len(short)-1,-1):
            if jinwei+int(short[i])+int(long[i])==0:
                jinwei = 0
                r1.append('0')
            elif jinwei+int(short[i])+int(long[i])==1:
                jinwei = 0
                r1.append('1')
            elif jinwei+int(short[i])+int(long[i])== 2:
                jinwei = 1
                r1.append('0')
            else:
                jinwei = 1
                r1.append('1')
        r1.reverse()
        print(r1)

        qian = list(long[0:len(long)-len(short)])

        # print(qian)
        # print(list( range(-1,-len(long)+len(short)-1,-1)))
        #前面几位与进位加和
        r2 = []
        for i in range(-1,-len(long)+len(short)-1,-1):
            if jinwei == 0:
                return ''.join(qian+r1)
            else:
                for i in range(-1,-len(qian)-1,-1):
                    if jinwei+int(qian[i])==0:
                        r2.append('0')
                        jinwei = 0
                    elif jinwei+int(qian[i])==1:
                        r2.append('1')
                        jinwei = 0
                    else:
                        r2.append('0')
                        jinwei = 1
                r2.reverse()
                print(r2)
                print(jinwei)
                if jinwei == 0:
                    return ''.join(r2+r1)
                else:
                    return '1'+''.join(r2+r1)

s = Solution()
print(s.addBinary('101111','10'))





