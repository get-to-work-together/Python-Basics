#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jun 28 13:37:56 2022

@author: peter
"""

import unittest

from processor import Processor

class TestStringMethods(unittest.TestCase):

    def test_processor_display(self):
        p = Processor()
        p.keyPressed('1')
        p.keyPressed('2')
        p.keyPressed('3')
        actual = p.getDisplay()
        self.assertEqual('123', actual)

    def test_processor_add(self):
        p = Processor()
        p.keyPressed('1')
        p.keyPressed('+')
        p.keyPressed('3')
        p.keyPressed('=')
        actual = p.getDisplay()
        self.assertEqual('4', actual)

    def test_processor_subtract(self):
        p = Processor()
        p.keyPressed('1')
        p.keyPressed('−')
        p.keyPressed('3')
        p.keyPressed('=')
        actual = p.getDisplay()
        self.assertEqual('-2', actual)

if __name__ == '__main__':
    unittest.main()


