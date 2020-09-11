
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
    n, m = map(int, input().split())
    ab = [list(map(int, input().split())) for _ in range(m)]
    ab = [[a-1, b-1] for a, b in ab]

    uf = UnionFind(n)

    for a, b in ab:
        uf.unite(a, b)

    mx = 0
    for i in range(n):
        s = uf.size(i)
        if s > mx:
            mx = s

    print(mx)


if __name__ == "__main__":
    main()