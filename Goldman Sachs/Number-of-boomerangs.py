def dist(p1,p2):
    x1,y1=p1
    x2,y2=p2
    return (x1-x2)**2 + (y1-y2)**2
def numberOfBoomerangs(points) -> int:
    if len(points)<3:
        return 0
    count=0
    for i in range(len(points)):
        d1={}
        for j in range(len(points)):
            x = dist(points[i],points[j])
            if x in d1:
                count+=2*d1[x]
                d1[x]+=1
            else:
                d1[x]=1
    return count