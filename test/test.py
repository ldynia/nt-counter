#!/usr/bin/env python3

import sys
import os.path
import unittest
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), os.path.pardir)))
from src.statistics import Statistic

if __name__ == '__main__':
    unittest.main()


class AppTestCase(unittest.TestCase):

    FILE_PATH = '/app/test/data/dna.fsa'

    def test_nucleotides_count(self):
        data_fle = open(self.FILE_PATH)
        results = Statistic(data_fle).count_nucleotides()

        self.assertEqual(results['A'], 333)
        self.assertEqual(results['C'], 454)
        self.assertEqual(results['T'], 303)
        self.assertEqual(results['G'], 469)