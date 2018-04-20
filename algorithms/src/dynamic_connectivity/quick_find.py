class QuickFindUF:
    def __init__(self, n):
        self.id = []
        [self.id.append(i) for i in range(n)]


    def __validate(self, p):
        if p < 0 or p >= len(self.id):
            raise ValueError("Index %s is not between 0 and %s" %(p, len(self.id) - 1))

    def connected(self, p, q):
        '''
        Check if p and q are in the same component

        :param p:
        :param q:
        :return: True if p and q are in the same component, False otherwise
        '''
        self.__validate(p)
        self.__validate(q)

        return self.id[p] == self.id[q]

    def union(self, p, q):
        """
        Change all entries with id[p] to id[q]
        :param p:
        :param q:
        """
        p_id = self.id[p]
        q_id = self.id[q]

        for i in range(len(self.id)):
            if self.id[i] == p_id:
                self.id[i] = q_id