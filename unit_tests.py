#!/usr/bin/env python

import unittest
from Lachesis_assembly_formatter_for_TASSEL import is_a_cluster_sequence, get_group_number

class TestLachesisAssemblyFormatter(unittest.TestCase):

    def setUp(self):
        self.clust_header_1 = "Lachesis_group0__552_contigs__length_50808702"
        self.clust_header_2 = "Lachesis_group1__500_contigs__length_43501254"
        self.unordered_header_1 = "flattened_line_34564__unordered_in_group0"
        self.unordered_header_2 = "flattened_line_34580__unordered_in_group1"
        self.ungrouped_header_1 = "flattened_line_34584__unclustered"
        self.ungrouped_header_2 = "flattened_line_34582__unclustered"

    def test_is_a_cluster_sequence(self):
        self.assertTrue(is_a_cluster_sequence(self.clust_header_1))
        self.assertTrue(is_a_cluster_sequence(self.clust_header_2))
        self.assertFalse(is_a_cluster_sequence(self.unordered_header_1))
        self.assertFalse(is_a_cluster_sequence(self.unordered_header_2))
        self.assertFalse(is_a_cluster_sequence(self.ungrouped_header_1))
        self.assertFalse(is_a_cluster_sequence(self.ungrouped_header_2))

    def test_get_group_number(self):
        self.assertEqual(get_group_number(self.clust_header_1), 0)
        self.assertEqual(get_group_number(self.clust_header_2), 1)
        self.assertEqual(get_group_number(self.unordered_header_1), 0)
        self.assertEqual(get_group_number(self.unordered_header_2), 1)
        self.assertEqual(get_group_number(self.ungrouped_header_1), None)
        self.assertEqual(get_group_number(self.ungrouped_header_1), None)

if __name__ == "__main__":
    unittest.main()
