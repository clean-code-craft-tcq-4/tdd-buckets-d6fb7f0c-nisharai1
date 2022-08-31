import unittest
from driven_ranges import *


class TestCurrentDrivenRanges(unittest.TestCase):
    def test_two_values_in_range(self):
        self.assertNotEqual(current_samples([-1, 5]), '1-5, 2')
        self.assertEqual(current_samples([4, 5]), '4-5, 2')

    def test_single_current_samples(self):
        expected_current_counts = [{'current': 0, 'occurrence': 0}, {'current': 1, 'occurrence': 1},
                                   {'current': 2, 'occurrence': 1}, {'current': 3, 'occurrence': 1},
                                   {'current': 4, 'occurrence': 1}, {'current': 5, 'occurrence': 0}]
        self.assertEqual(current_individual_readings([1, 3, 4, 2]), expected_current_counts)
        expected_current_counts = [{'current': 0, 'occurrence': 0}, {'current': 1, 'occurrence': 1},
                                   {'current': 2, 'occurrence': 0}, {'current': 3, 'occurrence': 1},
                                   {'current': 4, 'occurrence': 0}, {'current': 5, 'occurrence': 0}]
        self.assertNotEqual(current_individual_readings([1, 2, 4, 2]), expected_current_counts)

    def test_consecutive_grouping(self):
        self.assertNotEqual(log_consecutive_groups([-1, 0, 2, 0, 1, 1]), [[-1], [2, 1]])
        self.assertEqual(log_consecutive_groups([1, 0, 2, 0, 1, 1]),  [[1], [2], [1, 1]])
        self.assertEqual(log_consecutive_groups([1, 0, 0, 0, 1, 1]), [[1], [1, 1]])

    def test_check_error(self):
        self.assertNotEqual(identify_error([0, -1, 250, 500, 2000, 4000]), [0, -1, 250, 2000, 500, 4000])
        self.assertEqual(identify_error([0, -1, 250, 500, 2000, 4000]), [0, -1, 250, 500, 4000])

    def test_current_data(self):
        self.assertEqual(current_data(0), 0)
        self.assertNotEqual(current_data(1), -1)
        self.assertEqual(current_data(-1), 0)
        self.assertNotEqual(current_data(400), -2)
        self.assertEqual(current_data(400), 2)
        self.assertEqual(current_data(-1200), -6)
        self.assertEqual(current_data(1400), 7)
        self.assertEqual(current_data(1600), 8)
        self.assertEqual(current_data(2400), 12)


