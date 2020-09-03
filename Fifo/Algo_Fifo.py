class Fifo():
    _file = [(0,0)]
    target = []
    def __init__(self,item):
        self.item = item

    def targeted(self):
        self.target.append(self._file[0])
        return self.target

    def algo(self):
        newFile = []
        for _ in range(len(self._file)):
            x = self._file[0][0]
            y = self._file[0][1]
            self.targeted()
            del self._file[0]

            if not x+1 > len(self.item):
                if not (x+1, y) in self.target:
                    if self.item[x][y] == self.item[x+1][y]:
                        newFile.append((x+1, y))
            
            if not x-1 < 0:
                if not (x-1, y) in self.target:
                    if self.item[x][y] == self.item[x-1][y]:
                        newFile.append((x-1, y))
                    
            if not y+1 > len(item[0]):
                if not (x, y+1) in self.target:
                    if self.item[x][y] == self.item[x][y+1]:
                        newFile.append((x, y+1))

            if not y-1 < 0:
                if not (x, y-1) in self.target:
                    if self.item[x][y] == self.item[x][y-1]:
                        newFile.append((x, y-1))
        return newFile

    def feu(self):
        while (len(self._file) > 0):
            self._file = self.algo()
        return (len(self.target))

item = [[1,1,1,3,2],[1,2,3,2,1],[1,1,3,1,2],[4,2,1,2,4]]

print(Fifo(item).feu())
