from PointClass import Point
from VectorClass import Vector

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
        if len(self.Xs)!=len(self.Ys):
            print("ERROR INVALID POINT DATA")
        for i,x in enumerate(Xs):
            self.Points.append(Point(Xs[i],Ys[i]))
    
    def plot(self,):
        import numpy as np
        import matplotlib.pyplot as plt

        # Fixing random state for reproducibility
        np.random.seed(19680801)


        N = 50
        x = np.random.rand(N)
        y = np.random.rand(N)
        colors = np.random.rand(N)
        area = (30 * np.random.rand(N))**2  # 0 to 15 point radii

        plt.scatter(x, y, s=area, c=colors, alpha=0.5)
        plt.show()