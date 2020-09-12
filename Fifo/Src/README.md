# Biggest Zone Find
I needed of compute the biggest group of neighboring numbers that are equal

I used FIFO and BFS algorithm 

# Algorithm 

### BiggestZoneFind initiation

```python 
def __init__(self, item):
    self.item = item 
    self.visited ={}
    self.neighbour = {0:0}

def __call__(self):
    return(self.compute())
```

I initialise:
* item = Array bidimensionaln
* visited = Save their cell for not reselection
* neighbour = Save the biggest zone find 

When create instance of class BiggestZoneFind the fonction __call__ is runed and return the variable **neighbour**

----------------

### BrowseArray function
```python
def BrowseArray(self):
    for x in range(len(self.item)):
        for y in range(len(self.item[0])):
            self.BFS(x,y)
```
BrowseArray browse the array bidimensional(item variable) and return the coordinates and pass them in BFS function argument

----------------

### BFS function
```python
def BFS(self,x,y):
    compteur = 0
        fifo = [(x,y)]
        val_courant = self.item[x][y]
```

I initialise:
* counter = number of the loop
* fifo = file
* val_courant = value of the "sommet"
* x = coordinates 
* y = coordinates

----------------

```python
while fifo:
    compteur += 1
    x = fifo[0][0]
    y = fifo[0][1]
    self.visited[str(x)+"-"+str(y)] = True
    del fifo[0]
```
The coordinates is marked for not reselection 

The first elements in the file is delete

----------------

```python            
if not x+1 > len(self.item)-1:
    if not self.visited.get(str(x+1)+"-"+str(y)):
        if item[x+1][y] == val_courant:
            fifo.append((x+1, y))
```
Checked if he have a values around

Checked if is not marked

Checked if the value is egal at val_courant

Appending the value in the **FIFO**

----------------

<img src="Screenshot.png">


