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
        long = []
        short = []
        if len_a>len_b:
            for i in range(len(a)):
                long.append(str(i))
    
            for i in range(len(b)):
                short.append(str(i))
        else:
            for i in range(len(b)):
                long.append(str(i))
            
            for i in range(len(a)):
                short.append(str(i))
        
        # print(long,type(long),type(long[0]))
        # print(short,type(short))

        
        len_short = len(short)
        len_long = len(long)
        jinwei = 0
        r1 = []
        for i in range(len_short):
            r1.append('0')
        for i,j in zip(range(len_short-1,-1,-1), range(len_long-1,-1,len_long-len_short+1)):
            print(short[i],long[j])
            if jinwei+int(short[i])+int(long[j]) == 0:
                r1[i] = '0'
                jinwei=0
            elif jinwei+int(short[i])+int(long[j]) == 1:
                r1[i] = '1'
                jinwei=0
            else:
                r1[i]= '0'
                jinwei = 1
        print(r1,type(r1))
        r2 = []
        for i in range(len_long-len_short):
            r2.append('0')
        if jinwei == 0:
            rr = long[0:len_long-len_short-1].append(r1)
            print(rr,type(rr))
            return ''.join(rr)
        else:
            for i in range(len_long-len_short-1,-1,-1):
                if jinwei+int(long[i])==2:
                    jinwei = 1
                    r2[i] = '0'
                else:
                    rr = long[0:len_long - len_short - 1].append(r1)
                    return ''.join(rr)
            return ''.join(r2).join(r1)


s = Solution()
print(s.addBinary('110','1'))



