from math import sqrt, acos, pi

class Point:
    def __init__(self,x,y):
        self.x=x
        self.y=y
    def get():
        return (self.x,self.y)
    
class Vector:
    def __init__(self,x,y):
        self.x=x
        self.y=y
        
    def norm(self):
        return sqrt(self.x**2 + self.y**2)

#Gets the interior angle of an nth degree polygon.
#Retuns half of this angle for this specific application
def getInteriorAngle(n):
    total=(n-2)*180
    return total/n

# Vector distance 
def getDistance(a,b):
    return sqrt( (a.x-b.x)**2 + (a.y-b.y)**2 )

# a,b and c are points of an angle, with b as its vertex.
# This forms a vector from b->a and b->c then returns the inner angle
def innerProduct(a,b,c):
    A=Vector( a.x-b.x, a.y-b.y )
    B=Vector( c.x-b.x, c.y-b.y )
    if ( A.norm() * B.norm() == 0 ): return 1
    return acos(round( (A.x*B.x + A.y*B.y) / (A.norm() * B.norm()) ,6)) * 180 / pi #Rounding because pythons not the best with precision

# Center of mass or "centroid"
def getCenter(A):
    totalX=sum([p.x for p in A])
    totalY=sum([p.y for p in A])
    length=len(A)
    return Point( totalX/length, totalY/length )
