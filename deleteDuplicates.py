#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2021/2/25 16:26
__author__ = "hanruobing"

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

#指针的写不出来
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        # 快慢指针
        if not head:
            return None
        fast, slow = head, head
        while fast:
            if fast.val != slow.val:
                slow.next = fast
                slow = slow.next
            fast = fast.next
        slow.next = None
        return head

s = Solution()
print(s.deleteDuplicates(ListNode(1,2,2,3)))