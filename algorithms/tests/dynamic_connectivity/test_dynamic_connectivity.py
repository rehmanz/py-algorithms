import os
import logging
import unittest
import algorithms

from algorithms.src.dynamic_connectivity.quick_find import QuickFindUF
from algorithms.src.dynamic_connectivity.quick_union import QuickUnionUF
from algorithms.src.dynamic_connectivity.weighted_quick_union import WeightedQuickUnionUF

LOGGER = logging.getLogger()

class DynamicConnectivityTest(unittest.TestCase):
    @classmethod
    def setUpClass(self):
        logging.basicConfig(level=logging.DEBUG)

        try:
            if "dynamic_connectivity" in os.getcwd():
                data_file = os.path.join(os.getcwd(), "data/tiny_uf.txt")
            else:
                data_file = "%s/algorithms/tests/dynamic_connectivity/data/tiny_uf.txt" %os.getcwd()

            with open(data_file, "r") as f:
                self.n = int(f.readline())
                self.objects_l = ([tuple(line.split()) for line in f])

            LOGGER.debug(self.objects_l)
        except Exception as e:
            raise ValueError("Could not open data file - %s" %e)

    def test_quick_find(self):
        quick_find_o = QuickFindUF(n=self.n)
        for t in self.objects_l:
            p = int(t[0])
            q = int(t[1])
            quick_find_o.union(p, q)
            LOGGER.debug("%s %s" %(p, q))

        for t in self.objects_l:
            p = int(t[0])
            q = int(t[1])
            self.assertTrue(quick_find_o.connected(p, q), "%s != %s" %(p, q))

    def test_quick_union(self):
        quick_union_o = QuickUnionUF(n=self.n)
        for t in self.objects_l:
            p = int(t[0])
            q = int(t[1])
            quick_union_o.union(p, q)
            LOGGER.debug("%s %s" %(p, q))

        for t in self.objects_l:
            p = int(t[0])
            q = int(t[1])
            self.assertTrue(quick_union_o.connected(p, q), "%s != %s" %(p, q))

    def test_weighted_quick_union(self):
        w_quick_union_o = WeightedQuickUnionUF(n=self.n)
        for t in self.objects_l:
            p = int(t[0])
            q = int(t[1])
            w_quick_union_o.union(p, q)
            LOGGER.debug("%s %s" %(p, q))

        for t in self.objects_l:
            p = int(t[0])
            q = int(t[1])
            self.assertTrue(w_quick_union_o.connected(p, q), "%s != %s" %(p, q))

    @classmethod
    def tearDownClass(self):
        pass

if __name__ == "__main__":
    unittest.main()