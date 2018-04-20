class QuickUnionUF:
    def __init__(self, n):
        self.id = []
        for i in range(n):
            self.id.append(i)

    def __validate(self, p):
        if p < 0 or p >= len(self.id):
            raise ValueError("Index %s is not between 0 and %s" %(p, len(self.id) - 1))

    # find the root of i
    def __root(self, i):
        self.__validate(i)

        while (i != self.id[i]):
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

        self.id[p_root] = q_root