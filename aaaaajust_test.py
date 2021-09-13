#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2021/09/13 16:26:21
__author__ = 'hanruobing'


#手写一遍检验
# def bubble(disorder_list):
#     #比较len(disorder_list)-1轮
#     for c in range(1,len(disorder_list)):
#         for index in range(0,len(disorder_list)-1):
#             if disorder_list[index]>disorder_list[index+1]:
#                 disorder_list[index],disorder_list[index+1] = disorder_list[index+1],disorder_list[index]
#     return disorder_list

# print(bubble([2,9,3,8,4,5]))

# def select(disorder_list):
#     for one in range(0,len(disorder_list)-1):
#         for  another in range(one+1,len(disorder_list)):
#             if disorder_list[one] > disorder_list[another]:
#                 disorder_list[one],disorder_list[another] = disorder_list[another] , disorder_list[one]
#     return disorder_list

# print(select([2,9,3,8,4,5]))