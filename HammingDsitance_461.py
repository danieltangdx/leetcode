# -*- coding: utf-8 -*-
"""
Created on Mon Dec 25 18:53:31 2017

@author: tdx
"""

class Solution:
    def hammingDistance(self, x, y):
        """
        :type x: int
        :type y: int
        :rtype: int
        """
        return bin(x^y).count('1')