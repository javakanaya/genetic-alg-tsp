import numpy as np

# node class
class Node:
    def __init__(self, id,  x, y):
        self.id = id
        self.x = x
        self.y = y
    
    def distance(self, dest):
        xDis = abs(self.x - dest.x)
        yDis = abs(self.y - dest.y)
        distance = np.sqrt((xDis ** 2) + (yDis ** 2))
        return distance
    
    def __repr__(self):
        # return "(" + str(self.x) + "," + str(self.y) + ")"
        return "(" + str(self.id) + ")"
    
    
