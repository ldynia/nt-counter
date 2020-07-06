#!/usr/bin/env python3

import json
import os.path
import sys
import unittest
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), os.path.pardir)))
from src.statistics import Statistic


class AppTestCase(unittest.TestCase):

    file = '/app/test/data/dna_one.fsa'
    filename = file.split('/')[-1]

    def test_is_dict(self):
        stats = Statistic(self.file)
        results = stats.count_nucleotides()

        self.assertTrue(type(results) is dict)

    def test_is_json(self):
        stats = Statistic(self.file)
        results = stats.count_nucleotides()
        try:
            json.dumps(results)
            is_json = True
        except Exception:
            is_json = False

        self.assertTrue(is_json)

    def test_nucleotides_count(self):
        stats = Statistic(self.file)
        results = stats.count_nucleotides()

        self.assertEqual(results[self.filename]['A'], 333)
        self.assertEqual(results[self.filename]['C'], 454)
        self.assertEqual(results[self.filename]['T'], 303)
        self.assertEqual(results[self.filename]['G'], 469)


if __name__ == '__main__':
    unittest.main()
