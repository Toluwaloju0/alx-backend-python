"""A module to test the utils packsge"""

import functools
from parameterized import parameterized
import unittest
from utils import access_nested_map


class TestAccessNestedMap(unittest.TestCase):
    """A tet class for acceess_nested_map"""
    @parameterized.expand([
        ({"a": 1}, ("a")),
        ({"a": {"b": 2}}, ("a")),
        ({"a": {"b": 2}}, ("a", "b"))
        ])
    def test_access_nested_map(self, nested_map, path):
        """The test to make sure the function works correctly"""
        self.assertEqual(access_nested_map(nested_map, path), nested_map.get(path))
