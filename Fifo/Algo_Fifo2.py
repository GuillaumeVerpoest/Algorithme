class BiggestZoneFind:
    def __init__(self, item):
        self.item = item
        self.visited = {}
        self.neighbour = {0:0}

    
    def __call__(self):
        self.BrowseArray()
        return(self.neighbour)
    
    def BrowseArray(self):
        for x in range(len(self.item)):
            for y in range(len(self.item[0])):
                self.BFS(x,y)

    def BFS(self,x,y):
        compteur = 0
        fifo = [(x,y)]
        val_courant = self.item[x][y]
        while fifo:
            compteur += 1
            x = fifo[0][0]
            y = fifo[0][1]
            self.visited[str(x)+"-"+str(y)] = True
            del fifo[0]
            
            if not x+1 > len(self.item)-1:
                if not self.visited.get(str(x+1)+"-"+str(y)):
                    if item[x+1][y] == val_courant:
                        fifo.append((x+1, y))
                        
            if not x-1 < 0:
                if not self.visited.get(str(x-1)+"-"+str(y)):
                    if item[x-1][y] == val_courant:
                        fifo.append((x-1, y))

            if not y+1 > len(self.item[0])-1:
                if not self.visited.get(str(x)+"-"+str(y+1)):
                    if item[x][y+1] == val_courant:
                        fifo.append((x, y+1))
        
            if not y-1 < 0:
                if not self.visited.get(str(x)+"-"+str(y-1)):
                    if item[x][y-1] == val_courant:
                        fifo.append((x, y-1))

        if self.neighbour.values()[0] <= compteur:
            self.neighbour = {val_courant: compteur}


item = [[1,1,1,3,2],[1,2,3,2,1],[1,1,3,1,2],[4,2,1,2,4]]


biggestZoneFind = BiggestZoneFind(item)

print(biggestZoneFind())

