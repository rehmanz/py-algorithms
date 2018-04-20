class WeightedQuickUnionUF:
    def __init__(self, n):
        self.id = []
        self.sz = []

        for i in range(n):
            self.id.append(i)
            self.sz.append(0)

    def __validate(self, p):
        if p < 0 or p >= len(self.id):
            raise ValueError("Index %s is not between 0 and %s" %(p, len(self.id) - 1))

    # find the root of i and make every other node in path point to it's grandparent (thereby halving path lenght)
    def __root(self, i):
        self.__validate(i)

        while (i != self.id[i]):
            self.id[i] = self.id[self.id[i]]
            i = self.id[i]
        return i

    def connected(self, p, q):
        '''
        Check if p and q are in the same component

        :param p:
        :param q:
        :return: True if p and q are in the same component, False otherwise
        '''
        self.__validate(p)
        self.__validate(q)

        return self.__root(p) == self.__root(q)

    def union(self, p, q):
        """
        Change all entries with id[p] to id[q]
        :param p:
        :param q:
        """
        p_root = self.__root(p)
        q_root = self.__root(q)

        if (p_root == q_root):
            return

        if self.sz[p_root] < self.sz[q_root]:
            self.id[q_root] = q_root
            self.sz[q_root] += self.sz[q_root]
        else:
            self.id[q_root] = p_root
            self.sz[p_root] += self.sz[q_root]