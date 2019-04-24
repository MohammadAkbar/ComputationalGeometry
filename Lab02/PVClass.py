import math
%matplotlib inline
import matplotlib.pyplot as plt
plt.style.use('seaborn-whitegrid')
import numpy as np
class Point:
    # ------ Varaiables START ----------------------- #
    x = 0.0
    y = 0.0
    # ------ Varaiables END ------------------------- #
    # ------ Constructor START ---------------------- #
    def __init__( self , x , y ):
        self.x = x
        self.y = y
    # ------ Constructor END ------------------------ #
    # ------ Print Functions START ------------------ #
    def __repr__(self):
        return "( %f , %f )" % (self.x, self.y)
    def __str__(self):
        return "( %f , %f )" % (self.x, self.y)
    # ------ Print Functions END -------------------- #
    def update(self , x , y):
        self.x = x
        self.y = y
        
class Vector:
    # ------ Varaiables START ----------------------- #
    x = 0.0
    y = 0.0
    # ------ Varaiables END ------------------------- #
    # ------ Constructor START ---------------------- #
    def __init__( self , x:float , y:float ):
        self.x = x
        self.y = y
    # ------ Constructor END ------------------------ #
    # ------ Print Functions START ------------------ #
    def __repr__(self):
        return "< %f , %f >" % (self.x, self.y)
    def __str__(self):
        return "< %f , %f >" % (self.x, self.y)
    def magnitude(self):
        return math.sqrt(self.x*self.x + self.y*self.y)
    # ------ Print Functions END -------------------- #
    
class Graph:
    Xs = []
    Ys = []
    Points = []
    def __init__( self , Xs , Ys ):
        self.x = Xs
        self.y = Ys
        if len(Xs)!=len(Ys):
            print("ERROR INVALID POINT DATA")
        for i,x in enumerate(Xs):
            Points.append(Point(Xs[i],Ys[i]))
    def plot(self):
        plt.plot(Xs, Ys, 'o', color='black');
    # ------ Print Functions END -------------------- #

def PP2V(a: Point , b: Point):
    return Vector(b.x-a.x,b.y-a.y)

def CrossProduct( a: Vector , b: Vector) -> float:
    return a.x * b.y - a.y * b.x

def DotProduct( a: Vector , b: Vector) -> float:
    return a.x * b.x + a.y * b.y

def IsCollinear( P1 : Point , P2 : Point , P3 : Point ) -> bool:
    return (P3.y - P2.y)*(P2.x - P1.x) - (P2.y - P1.y)*(P3.x - P2.x) == 0.0

def Relate( P1 : Point , P2 : Point , P3 : Point ):
    print( (P3.y - P2.y)*(P2.x - P1.x) - (P2.y - P1.y)*(P3.x - P2.x) )
    
def Intersection( P1 : Point , P2 : Point , P3 : Point , P4 : Point , P5 : Point ):
    D  = (P2.x - P1.x)*(P3.y - P4.y) - (P1.y - P2.y)*(P4.x - P3.x)
    Dx = (P1.y*P2.x - P1.x*P2.y)*(P3.y - P4.y) - (P1.y - P2.y)*(P3.y*P4.x - P3.x*P4.y)
    Dy = (P2.x - P1.x)*(P3.y*P4.x - P3.x*P4.y) - (P1.y*P2.x - P1.x*P2.y)*(P4.x - P3.x)
    if D == 0.0 and Dx != 0.0 and Dy != 0.0:
        return 1
    elif D == Dx == Dy == 0.0:
        return 2
    else:
        P5.update( Dx/D , Dy/D)
        return 3
