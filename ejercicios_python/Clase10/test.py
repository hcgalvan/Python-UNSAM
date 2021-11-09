# -*- coding: utf-8 -*-
"""
Created on Mon Nov  8 08:12:55 2021

@author: User
"""

class Person:
    def __init__(self,name,age):
        self.name = name
        self.age = age

    def __getitem__(self, key):
        print ("Inside `__getitem__` method!")
        #return getattr(self,key)
        return self.__getitem__(key)
