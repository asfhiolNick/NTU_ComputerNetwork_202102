import numpy as np

class Topo:

    def __init__(self, filename):
        self.filename = filename
        f = open(self.filename, 'r')
        i = 0

        for line in f.readlines():
            if i == 0:
                self.numNodes = int(line)
                i = 1
                self.links = np.zeros((self.numNodes, self.numNodes))
            else:
                tokens = line.split()
                self.links[int(tokens[0])][int(tokens[1])] = int(tokens[2])
                self.links[int(tokens[1])][int(tokens[0])] = int(tokens[2])

    def printLinks(self):
        for i in range(self.numNodes):
            for j in range(self.numNodes):
                if self.links[i][j] > 0:
                    print(i, '-->', j, '\t', self.links[i][j])

