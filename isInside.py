try:
    from util import *
except Exception:
    from inside.util import *
    

# A and B are tuple arrays of shapes.
# Returns true if shape A is completly contained within shape B
def isInside(A,B):
    
    #Convert tuple array into points for readability.
    A=[Point(p[0],p[1]) for p in A]
    B=[Point(p[0],p[1]) for p in B]
    
    #Get centroid of the potentially inner shape, A
    center=getCenter(A)

    #Get half the  inner angle of the polygons
    innerAngle=getInteriorAngle(len(A))/2

    #See if every point in B is within A
    for b in B:
        #vertex is the closest vertex to the test point
        vertex=sorted([(getDistance(a,b),a) for a in A], key=lambda p:p[0])[0][1]
        
        angle=innerProduct(center,vertex,b)
        lengthA=getDistance( center, vertex )
        lengthB=getDistance( center, b )
        if round(lengthA-lengthB,6)==0: continue
        if lengthA<lengthB or angle>innerAngle:
            return False
    return True
