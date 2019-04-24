import math
import matplotlib.pyplot as plt
import matplotlib.lines as lines
#plt.style.use('seaborn-whitegrid')
import numpy as np
from pylab import *
import functools
import copy

class Point:
    x = 0.0
    y = 0.0
    def __init__( self , x , y ):
        self.x = x
        self.y = y
    def __repr__(self):
        return "( %f , %f )" % (self.x, self.y)
    def __str__(self):
        return "( %f , %f )" % (self.x, self.y)
    def update(self , x , y):
        self.x = x
        self.y = y
        
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

class Graph:
    
    Xs = []
    Ys = []
    Points = []
    S = []
    gcenterx = 0.0
    gcentery = 0.0
    
    def __init__( self , Xs , Ys ):
        self.Xs = Xs
        self.Ys = Ys
        self.Points = []
        self.S = []
        self.gcenterx = 0.0
        self.gcentery = 0.0
        if len(self.Xs)!=len(self.Ys):
            print("ERROR INVALID POINT DATA")
        for i,x in enumerate(Xs):
            self.Points.append(Point(Xs[i],Ys[i]))

    def __repr__(self):
        output = ""
        for i,p in enumerate(self.S):
            if(i>0):
                output+=","
            output+= "( %g , %g )" % (p.x, p.y)
        return output
    def __str__(self):
        output = ""
        for i,p in enumerate(self.S):
            if(i>0):
                output+=","
            output+= "( %g , %g )" % (p.x, p.y)
        return output
    
    def connectpoints(x,y,p1,p2):
        x1, x2 = x[p1], x[p2]
        y1, y2 = y[p1], y[p2]
        plt.plot([x1,x2],[y1,y2],'k-')
    
    def plot2(self , ccwlines , numbered , hull):
        y = [p.y for p in self.Points]
        x = [p.x for p in self.Points]
        n = [n for n,p in enumerate(self.Points)]
        # plot points
        fig, ax = plt.subplots(figsize = (10, 10))
        ax.scatter(x , y , 100, 'orange', zorder=3)
        ax.scatter(self.gcenterx , self.gcentery , 100, 'red', zorder=9)
        ax.axis('scaled')
        
        # number points
        if(numbered):
            for i, txt in enumerate(n):
                offset = 0.1
                ax.annotate(-txt+len(n)-1, (x[i]+offset, y[i]+offset), horizontalalignment='center', verticalalignment='center',fontsize=15)
                
        # lines from origin
        if ccwlines:
            for p in self.Points:
                l = [(p.x,p.y), (self.gcenterx,self.gcentery)]
                (lxs, lys) = zip(*l)
                ax.add_line(Line2D(lxs, lys, linewidth=1.5, color='blue', zorder=2))
                
        if hull:
            for i,p in enumerate(self.S):
                ax.scatter(p.x , p.y , 100, 'springgreen', zorder=4)
                l = [(p.x,p.y), (self.S[i-1].x,self.S[i-1].y)]
                (lxs, lys) = zip(*l)
                ax.add_line(Line2D(lxs, lys, linewidth=3, color='springgreen', zorder=4))
        
    def bottom_left(self):
        minidx = -1
        minval = float("inf")
        for i , p in enumerate(self.Points):
            x = p.x
            y = p.y
            if y < minval:
                minval = y
                minidx = i
            elif y == minval:
                if self.Points[i].x < self.Points[minidx].x:
                    minidx = i
        self.gcenterx = self.Points[minidx].x
        self.gcentery = self.Points[minidx].y
        return minidx
    
    def sort_ccw(self , bl):
        P = copy.deepcopy(self.Points)
        origin = P.pop(bl)
        self.Points = sorted(P, key=functools.cmp_to_key(self.compare_point2))
        self.Points.append(origin)
        
    def scan(self):
        P = copy.deepcopy(self.Points)
        S = []
        S.append(P.pop())
        S.append(P.pop())
        S.append(P.pop())
        while len(P)>0:
            pi = P.pop()
            while self.ccw(S[-2],S[-1],pi) < 1:
                S.pop()
            S.append(pi)
        self.S = S
    
    def ccw(self, p0: Point , p1: Point, p2: Point):
        a , d = p0.x , p0.y
        b , e = p1.x , p1.y
        c , f = p2.x , p2.y
        g , h , i = 1 , 1 , 1
        det1 = a*(e*i - f) - b*(d*i - f) + c*(d - e)
        if det1 > 0:
            return 1
        elif det1 < 0:
            return -1
        else:
            return 0
    def compare_point2(self, p1:Point, p2: Point):
        a , d = self.gcenterx , self.gcentery
        b , e = p1.x , p1.y
        c , f = p2.x , p2.y
        g , h , i = 1 , 1 , 1
        det1 = a*(e*i - f) - b*(d*i - f) + c*(d - e)
        if det1 > 0:
            return 1
        elif det1 < 0:
            return -1
        else:
            return 0
