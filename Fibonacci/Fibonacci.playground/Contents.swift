class Fibonacci {
    var n:Int
    init(n:Int){
        self.n = n
    }
    
    // MARK: - RECURSIVE
    fileprivate func recursive(n:Int) -> Int{
        if n == 0 {
            return 0
        }else if n == 1{
            n == 1
            return 1
        }else{
            return recursive(n: n-1) + recursive(n: n-2)
        }
    }
    
    
    // MARK: - BOTTOMTOP
    fileprivate func bottomTop() -> Int{
        var array = [0,1]
        for index in Range(2...self.n){
            array.append(0)
            array[index] = array[index-1] + array[index-2]
        }
        return array[self.n]
    }
    
    
    // MARK: - ITERATION
    fileprivate func iteration() -> Int{
        var cpt: Int = self.n-1
        var first: Int = 0
        var seconde: Int = 1
        var tmp: Int
        while cpt >= 0 {
            tmp = first+seconde
            first = seconde
            seconde = tmp
            cpt -= 1
        }
        return first
    }
}

let instance = Fibonacci(n:16)

print("Recursive -> " ,instance.recursive(n: instance.n))
print("Bottom_top -> " ,instance.bottomTop())
print("iteration -> " ,instance.iteration())

