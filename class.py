#!/usr/bin/python
# -*- coding: utf-8 -*-

class MyClass(object):
    message = 'Hello, Developer'
    
    def show(self):
        print self.message 
        
    def __init__(self, name = 'unset', color = 'black'):
        print 'Constructor is called with params: ', name, ' ', color 

inst = MyClass()
inst.show()

inst2 = MyClass('David')
inst2.show()