from math import pi,cos,sin
import sys
try:
    from isInside import isInside
except Exception:
    from inside.isInside import isInside

data=None
with open(sys.argv[1]) as f:
    data=f.read()

#matplotlib helper
#def plot(shape):
#    plt.plot([x[0] for x in shape],[y[1] for y in shape])

data=data.split('\n')
entries=[]
for datum in data:
    if '#' not in datum and datum != '' and 'Reuleaux' not in datum:
        entries.append(datum.split(' '))

def circleToPolygon(center,radius,precision=20):
    points=[]
    for i in range(precision):
        angle=i*2*pi/(precision-1)
        points.append((center[0]+cos(angle)*radius, center[1]+sin(angle)*radius))
    return points
        
params=[]
answers=[]
for entry in entries:
    limit=None
    shape=None
    param=[]
    case=[]
    truth=None
    for item in entry:
        if('Circle' in item):
            #setup circle 2 entries
            limit=2
            shape='circ'
        elif('Triangle' in item):
            #setup triangle 3 entries
            limit=3
            shape='tri'
        elif('Pentagon' in item):
            #setup pentagon 5 entries
            limit=5
            shape='pent'
        elif('Reuleaux' in item):
            #setup reuleaux 3 entries
            limit=3
            #removed for now...
        else:
            #this is actually data
            if(',' in item):
                #point
                point=item.split(',')
                param.append((float(point[0]),float(point[1])))
            elif 'true' in item or 'false' in item:
                answers.append(item)
                truth=item
            else:
                #radius
                param.append(float(item))
        if len(param) == limit:
            if(shape=='circ'):
                case.append(circleToPolygon(param[0],float(param[1])))
            elif(shape=='tri'):
                case.append(param)
            elif(shape=='pent'):
                case.append(param)
            else:
                print("test")
            limit=None
            shape=None
            param=[]
            truth=None

    params.append(case)

for i,param in enumerate(params):
    value=str(isInside(param[1],param[0])).lower()
    if(value==answers[i]):
        print("Success", answers[i])
    else:
        print("Fail!", answers[i], value)
