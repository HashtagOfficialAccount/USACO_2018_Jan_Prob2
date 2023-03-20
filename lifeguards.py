x = open("lifeguards.in", 'r')
N = int(x.readline().strip())
l = [x.readline().strip().split() for i in range(N)]
x.close()
times = []
index = 0
for cow in l:
    temp = l[:]
    temp.pop(index)
    t = []
    for i in temp:
        for o in range(int(i[0]),int(i[1])):
            t.append(o)
    times.append(len(set(t)))
    index += 1
    
y = open("lifeguards.out",'w')
y.write(str(max(times)))
y.close()
