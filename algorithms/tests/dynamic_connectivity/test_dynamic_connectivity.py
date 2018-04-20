import logging
import unittest
import algorithms

from algorithms.src.dynamic_connectivity.quick_find import QuickFindUF

LOGGER = logging.getLogger()

class DynamicConnectivityTest(unittest.TestCase):
    @classmethod
    def setUpClass(self):
        logging.basicConfig(level=logging.DEBUG)

        with open("data/tiny_uf.txt", "r") as f:
            self.n = int(f.readline())
            self.objects_l = ([tuple(line.split()) for line in f])

        LOGGER.debug(self.objects_l)

    def test_quick_find(self):
        quick_find_o = QuickFindUF(n=self.n)
        for t in self.objects_l:
            p = int(t[0])
            q = int(t[1])
            quick_find_o.union(p, q)
            LOGGER.debug("%s %s" %(p, q))

            self.assertTrue(quick_find_o.connected(p, q))

    @classmethod
    def tearDownClass(self):
        pass

if __name__ == "__main__":
    unittest.main()