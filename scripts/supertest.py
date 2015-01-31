#!/usr/bin/env python
class Top(object):
    def __init__(self):
        print "Top:",type(self)

    def first(self):
        print "Top First:",type(self)
        self.__second()

    def __second(self):
        print "Top Second:",type(self)

class Bottom(Top):
    def __init__(self):
        print "Bottom:",type(self)

    def first(self):
        print "Bot First",type(self)
        super(Bottom,self).first()

    def __second(self):
        print "Bot Second",type(self)

a=Bottom()
a.first()
