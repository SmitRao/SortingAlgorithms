#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Apr 18 15:52:15 2018

@author: smitrao
"""

def merge(l1: list, l2: list) -> list:
    i = 0
    j = 0
    merged = []
    while (i < len(l1) and j < len(l2)):
            if l1[i] < l2[j]:
                    merged.append(l1[i])
                    i += 1
            elif l1[i]>l2[j]:
                    merged.append(l2[j])
                    j += 1
            else:
                    merged += [l1[i], l2[j]]
                    i += 1
                    j += 1
    if i < len(l1):
            merged += l1[i:]
    elif j<len(l2):
            merged += l2[j:]
    return merged

def merge_sort(l: list) -> list:
    if len(l) < 2:
        return l
    elif len(l) == 2:
        if l[0] >= l[1]:
            return [l[1], l[0]]
        else:
            return [l[0], l[1]]
    else:
        part1 = merge_sort(l[0:len(l)//2])
        part2 = merge_sort(l[len(l)//2: len(l)])
        return merge(part1, part2)
    
    
    

if __name__ == '__main__':
    print("\nSort ['b', 'c', 'z', 'e', 'f', 'd', 'a', 'b', 'a']:\n", \
          merge_sort(['b', 'c', 'z', 'e', 'f', 'd', 'a', 'b', 'a']), sep='')
    print("\nSort [1, 56, 6, 89, 16]:\n", \
          merge_sort([1, 56, 6, 89, 16]), sep='')
    print("\nSort []:\n", \
          merge_sort([]), sep='')
    print("\nSort [1]:\n", \
          merge_sort([1]), sep='')