#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2021/3/13 21:33
__author__ = "hanruobing"

class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        ss = s.lower()
        li = []
        al = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
        num = ['0','1','2','3','4','5','6','7','8','9']
        for i in ss:
            if i in al or i in num:
                li.append(i)

        re_li = li[::-1]

        if li == re_li:
            return True
        else:
            return False