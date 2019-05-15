#!/usr/bin/env

from PointClass import Point
from VectorClass import Vector

class Graph:
    
    
    
    # START ------------------------------__init__------------------------------------- START
    def __init__( self , Xs , Ys, Title ):
        self.Xs = Xs
        self.Ys = Ys
        self.Points = []
        self.Hull = []
        self.Title = Title
        if len(self.Xs)!=len(self.Ys):
            print("ERROR INVALID POINT DATA")
        for i,x in enumerate(Xs):
            self.Points.append(Point(Xs[i],Ys[i]))
    # END --------------------------------__init__--------------------------------------- END
    
    
    
    # START -----------------------------ConvexHull------------------------------------ START
    def ConvexHull(self):
        # load point data
        P = self.Points
        
        # edge case, only one point
        if len(P) <= 1:
            return P
        
        # sort points based on x value , then y value to break ties
        S = sorted(P, key = lambda pi: (pi.x, pi.y))
        
        # left-right direction helper function
        def direction(A,B,C):
            return (B.x - A.x) * (C.y - A.y) - (B.y - A.y) * (C.x - A.x)
        
        # compute upper hull
        U = []
        for i,si in enumerate(S):
            while len(U) >= 2 and direction(U[-2],U[-1],si) > 0:
                U.pop()
            U.append(si)
            
        # compute lower hull
        L = []
        for i,si in enumerate(S):
            while len(L) >= 2 and direction(L[-2],L[-1],si) < 0:
                L.pop()
            L.append(si)
            
        # remove duplicates
        L , U = L[:-1] , U[1:]
        
        # fix order CW -> CCW
        U.reverse()
        
        # save hull to class variable
        self.Hull = L + U
        
        # return the convex hull
        return self.Hull
    # END --------------------------------ConvexHull------------------------------------ END
    
    
    
    # START --------------------------------plot--------------------------------------- START
    def plot(self,numbered=True,hull=True):
        from matplotlib import pyplot as plt
        
        # data for graph
        y = [p.y for p in self.Points]
        x = [p.x for p in self.Points]
        n = [n for n,p in enumerate(self.Points)]
        
        # size of the graph
        plt.figure(figsize=(10,10))

        # main scatterplot
        plt.scatter(x , y , 500, 'lightblue', zorder=3)
        
        # numbered points
        if(numbered):
            for i, txt in enumerate(n):
                offset = -0.02
                message = "%g,%g" % (x[i], y[i])
                plt.annotate(message, (x[i], y[i]+offset), horizontalalignment='center', verticalalignment='center',fontsize=12, zorder=5,color='lightseagreen')
        
        # show the hull
        if hull:
            for i,p in enumerate(self.Hull):
                plt.scatter(p.x , p.y , 500, 'springgreen', zorder=4)
                l = [(p.x,p.y), (self.Hull[i-1].x,self.Hull[i-1].y)]
                (lxs, lys) = zip(*l)
                plt.plot(lxs, lys, linewidth=3, color='springgreen', zorder=4)        
        
        
        
        # labels and titles and text stuff
        plt.xlabel('x - axis',color='tomato') 
        plt.ylabel('y - axis',color='tomato') 
        plt.title(self.Title,color='lightcoral') 
        
        # Hide grid lines
        #plt.grid(False)
        #plt.axis('off')

        plt.show() 
    # END ----------------------------------plot----------------------------------------- END
