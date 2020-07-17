class Fibonacci {
    var n:Int
    // MARK: - INITIALISATION
    init(n:Int) {
        self.n = n
    }
    
    // MARK: -RECURSIVE
    func recursive(n:Int = instance.n) -> Int
    {
        if n == 0
        {
            return 0
        }
        else if n == 1
        {
            return 1
        }
        else
        {
            return recursive(n:n-1) + recursive(n:n-2)
        }

    }
    // MARK: - BOTTOM_TOP
    func bottom_top(n:Int = instance.n) -> Int
    {
        var array = [0,1]
        for index in Range(2...n) {
            array.append(0)
            array[index] = array[index-1] + array[index-2]
        }
        return array[n]
    }
    // MARK: - ITERATION
    func iteration(i:Int = instance.n) ->Int
    {
        var cpt: Int = n-1
        var first: Int = 0
        var seconde: Int = 1
        var tmp:Int
        while cpt >= 0
        {
            tmp = first+seconde
            first = seconde
            seconde = tmp
            cpt -= 1
        }
        return first
    }
}

var instance  = Fibonacci(n:16)
print("Recursive -> ",instance.recursive())
print("Bottom_top -> ",instance.bottom_top())
print("iteration -> ", instance.iteration())




//array 2 dimmension
//horizontal - vertical
//3 index
// 1->3
// combien de 1 sont côte a côte 
