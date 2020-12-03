#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2020/12/3 22:08
__author__ = "hanruobing"

class Solution(object):
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """

        if l1==[]:
            return l2
        if l2==[]:
            return l1

        r = []
        for i in range(min(len(l1),len(l2))):
            if l1[i]<=l2[j]:
                r.append(l1[i])
            else:
                r.append(l2[j])