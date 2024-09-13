#!/usr/bin/env python3
"""
    
"""

from parameterized import parameterized, parameterized_class


import unittest
from utils import access_nested_map

class TestAccessNestedMap(unittest.TestCase):

    @parameterized.expand( [ ({"a": 1}, ("a",), 1), ({"a": {"b": 2}}, ("a",), {"b": 2}), ({"a": {"b": 2}}, ("a", "b"), 2), ])
    def test_access_nested_map(self, nested_map, path, expected):
        self.assertEqual(access_nested_map(nested_map, path), expected)

    @parameterized.expand([({}, ("a",), 'a'),({"a": 1}, ("a", "b"), 'b')])
    def test_access_nested_map_exception(self, map, path, wrong_output):
        """ Test method raises correct exception """
        with self.assertRaises(KeyError) as e:
            access_nested_map(map, path)
            self.assertEqual(wrong_output, e.exception)



if __name__ == '__main__':
    unittest.main()
