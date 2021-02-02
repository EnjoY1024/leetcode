#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2020/12/3 22:08
__author__ = "hanruobing"


# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


class Solution:
    def mergeTwoLists(self, l1, l2):
        if l1 is None:
            return l2
        elif l2 is None:
            return l1
        elif l1.val < l2.val:
            l1.next = self.mergeTwoLists(l1.next, l2)
            return l1
        else:
            l2.next = self.mergeTwoLists(l1, l2.next)
            return l2


s = Solution()
print(s.mergeTwoLists([1,2,4],[1,3,4]))