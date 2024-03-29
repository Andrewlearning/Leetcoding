### Union find 介绍
ref: https://www.youtube.com/watch?v=YKE4Vd1ysPI
这种数据结构的作用是检测一个图有没有环， 假如说有环，那么并查集里不只有一个最顶节点

例如我们存在一个图
```
0----1----2---5
     |    |
     4    6
```
中心思想上是， 把能通过链接来访问到的各种点，放到一个集合里面去
例如（0，1，2，4，5，6）从任意一个点出发都能到达集合内的任意另一个点

那么假如说集合里的任意两个元素中间再相连，例如[4,6]，则会产生环
我们能使用这个规律，解决261/684问题

Find：找到某节点的最父亲节点，确定元素属于哪一个子集。它可以被用来确定两个元素是否属于同一子集。
Union：将两个子集合并成同一个集合。

```
a<---b<--c<--d
e<---f<--g
```
我们可以想象，每个集合分配好以后存在一个老大，在这里一个是a,一个是e


### Union find 的两种优化方法
我们一般使用两种优化方法
1. 路径压缩 `Path compression`，一般面试只写这种就好了
   - 在哪里：一般使在find函数里面编写
   - 作用是：把每个节点都指向它的最父节点，那么能使这个树的深度最低, 使find的时间复杂度下降成O(1)
2. union by rank
    - 合并时将元素所在深度小的集合合并到元素所在深度大的集合
      - 例如一棵高度为2的树，和一个高度为3的树，那么高度为2的树就要融合到高度为3的树上去
    - 作用是：降低合并后树的高度，减少find的次数


## Union find的各种写法
参考: 古城算法 https://www.youtube.com/watch?v=gBmwoxsL8lY
### 朴素模板
```
class UF:
    def __init__(self, M):
        n = len(M)
        self.parent = [i] * n

    # 朴素做法
    # 每次都根据一个节点一步步找它的父节点
    def find(self, x):
        if x.parent == x:
            return x
        else:
            return self.find(x.parent)


    def union(self, p, q):
        proot = self.find(p)
        qroot = self.find(q)

        # 假如两个的根节点不想等，我们可以指认任意一个根节点是另一个根节点的父亲
        self.parent[proot] = qroot
```

### Path compression 路径压缩模板
例题: 547，990

一般 解题/面试 用这个就已经足够了
```
class UF:
    def __init__(self, M):
        n = len(M)
        self.parent = [i] * n

    # Time O(1)
    # 当一个node 不是指向自己的时候，那么它就要一直向上找，直到找到根节点
    # 这种写法等于做了路径压缩，等于一路一直把自己的父节点都指向了根节点
    def find(self, x):
        if x != self.parent[x]:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]


    # union这里，不考虑结构的话，谁的做谁的父亲问题都不大
    # 一个问题，两个节点union后，会改变其中一个根节点指向，假如说不再次对所有节点进行
    find,那么无法达到所有节点都指向同一个父亲，例如323题
    def union(self, p, q):
        proot = self.find(p)
        qroot = self.find(q)

        # 假如说两者的根节点相等，那么我们什么都不操作
        if proot == qroot:
            return

        # 假如两个的根节点不想等，我们可以指认任意一个根节点是另一个根节点的父亲
        self.parent[proot] = qroot
```

### 路径压缩和union by rank都做了的版本：
```
class UF:
    def __init__(self, n):
        self.parent = [i for i in range(n+1)]
        self.rank = [1] * (n+1)

    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, p, q):
        proot, qroot = self.find(p), self.find(q)
        if proot == qroot:
            return

        # p的深度高的话， 那么要把q连到p上
        if self.rank[proot] > self.rank[qroot]:
            self.parent[qroot] = proot

        # q的深度高的话， 那么要把p连到q上
        elif self.rank[proot] > self.rank[qroot]:
            self.parent[proot] = qroot
        # 深度一样的那就随意了，做老爸的rank +1
        else:
            self.parent[proot] = qroot
            self.rank[proot] += 1
```

