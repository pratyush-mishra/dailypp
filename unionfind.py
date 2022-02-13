
#quick find implementation in which finding a connection takes O(1) time but making a connection takes O(N)

class QF:
    def __init__(self, n):
        self.id = [*range(0,n)] #we use * operator to unpack the type range and add it to an attribute id of type list
    
    def connected(self, a, b): #O(1) time complexity
        return self.id[a] == self.id[b]

    def union(self, a, b): #time complexity O(N)
        aid = self.id[a]
        bid = self.id[b]
        print(aid)
        print(bid)
        for i in self.id:
            if(self.id[i] == aid):
                self.id[i] = bid

qf = QF(5)


#Quick union implementation which optimizes union but worsens find


class QU:
    def __init__(self, n):
        self.id = [*range(0,n)]
    
    def root(self, a):
        while(self.id[a] != a):
            a = self.id[a]
        return a
    
    def connected(self, a, b): #O(N) time complexity
        return self.root(a) == self.root(b)
    
    def union(self, a, b): #O(N) time complexity
        roota = self.root(a)
        rootb = self.root(b)
        self.id[roota] = rootb


