#!/usr/bin/env
class Point:
    x = 0.0
    y = 0.0
    def __init__( self , x , y ):
        self.x = x
        self.y = y
    def __repr__(self):
        return "( %g , %g )" % (self.x, self.y)
    def __str__(self):
        return "( %g , %g )" % (self.x, self.y)
    def update(self , x , y):
        self.x = x
        self.y = y