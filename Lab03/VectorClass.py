class Vector:
    x = 0.0
    y = 0.0
    def __init__( self , x:float , y:float ):
        self.x = x
        self.y = y
    def __repr__(self):
        return "< %f , %f >" % (self.x, self.y)
    def __str__(self):
        return "< %f , %f >" % (self.x, self.y)
    def magnitude(self):
        return math.sqrt(self.x*self.x + self.y*self.y)
    # ------ Print Functions END -------------------- #