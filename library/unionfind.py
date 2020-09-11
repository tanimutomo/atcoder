

class UnionFind:
    def __init__(self, n :int):
        self.d = [-1] * n

    def find(self, x :int) -> int:
        if self.d[x] < 0: return x
        return self.find(self.d[x])
    
    def unite(self, x, y :int):
        xr, yr = self.find(x), self.find(y)
        if xr == yr:
            return

        if -self.d[xr] < -self.d[yr]:
            xr, yr = yr, xr

        self.d[xr] += self.d[yr]
        self.d[yr] = xr

    def is_same(self, x, y :int) -> bool:
        return self.find(x) == self.find(y)

    def size(self, x :int) -> int:
        return - self.d[self.find(x)]


def main():
    n = 12
    edges = [
        [1, 2], [5, 2], [6, 2], [12, 3],
        [3, 9], [9, 8], [4, 7], [10, 1],
    ]
    edges = [[i-1, j-1] for i,j in edges]

    uf = UnionFind(n)
    for i, j in edges:
        uf.unite(i, j)

    print(uf.find(5-1)+1)
    print(uf.size(5-1))
    print(uf.is_same(5-1, 10-1))


if __name__ == "__main__":
    main()