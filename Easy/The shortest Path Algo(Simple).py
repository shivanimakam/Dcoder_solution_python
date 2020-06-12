import math
ax,ay,bx,by=list(map(int,input().split()))
xdist=math.sqrt(ax*ax+ay*ay)
ydist=math.sqrt(bx*bx+by*by)
if xdist>ydist:
    print("B")
else:
    print("A")
