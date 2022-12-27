from topo import Topo
import numpy as np
import sys

start = 0
inf = 9999999999

myTopo = Topo(sys.argv[1])
#myTopo = Topo('input.txt')
#myTopo = Topo('input_2.txt')

N = np.zeros((myTopo.numNodes, 1))
D = np.zeros((myTopo.numNodes, 1))
p = np.zeros((myTopo.numNodes, 1))

for i in range(myTopo.numNodes):
    D[i] = inf
    p[i] = -1
    #N[i] = -1

D[start] = 0
p[start] = start
N[0] = 1

# TODO: your codes here
for i in range(myTopo.numNodes):
    if myTopo.links[start][i]!=0:
        D[i], p[i] = myTopo.links[start][i], start

for i in range(myTopo.numNodes):
    min, u = inf, -1
    for j in range(myTopo.numNodes):
        if N[j] == 0 and D[j] < min:
            min, u = D[j], j
    N[u] = 1

    for v in range(myTopo.numNodes):
        if myTopo.links[u][v]!=0:
            if D[u]+myTopo.links[u][v] < D[v]:
                D[v], p[v] = D[u]+myTopo.links[u][v], u
###


for i in range(1, myTopo.numNodes):
    print(int(p[i]), ' --> ', i, ' cost = ', int(D[i]))


