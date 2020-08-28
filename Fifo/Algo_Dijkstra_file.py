item = [[1,1,1,3,2],[1,2,3,2,1],[1,1,3,1,2],[4,2,1,2,4]]

_file = [(0,0)]
marque = []

def marquage():
    marque.append(_file[0])
    return marque

def algo(_file):
    newFile = []
    for _ in range(len(_file)):

        x = _file[0][0]
        y = _file[0][1]
        marquage()
        del _file[0]

        if not x+1 > len(item):
            if not (x+1, y) in marque:
                if item[x][y] == item[x+1][y]:
                    newFile.append((x+1,y))

        if not x-1 < 0:
            if not (x-1, y) in marque:
                if item[x][y] == item[x-1][y]:
                    newFile.append((x-1,y))

        if not y+1 > len(item[0]):
            if not (x, y+1) in marque:
                if item[x][y] == item[x][y+1]:
                    newFile.append((x,y+1))

        if not y-1 < 0:
            if not (x, y-1) in marque:
                if item[x][y] == item[x][y-1]:
                    newFile.append((x,y-1))
    return newFile

while (len(_file) > 0):
     _file = algo(_file)
    
print(len(marque))


