#!/usr/bin/env python3
"""A module to test the utils packsge"""

import functools
from parameterized import parameterized
import unittest
from utils import access_nested_map


class TestAccessNestedMap(unittest.TestCase):
    """A tet class for acceess_nested_map"""
    def get_item(self, nested_map, path):
        """A function to get the item at path"""

        for key in path:
            nested_map = nested_map.get(key)
            if nested_map is None:
                raise KeyError(key)
        return nested_map

    @parameterized.expand([
        ({"a": 1}, ("a")),
        ({"a": {"b": 2}}, ("a")),
        ({"a": {"b": 2}}, ("a", "b"))
        ])
    def test_access_nested_map(self, nested_map, path):
        """The test to make sure the function works correctly"""
        self.assertEqual(access_nested_map(nested_map, path),
                         self.get_item(nested_map, path))

    @parameterized.expand([
        ({}, ("a")),
        ({"a": 1}, ("a", "b"))
    ])
    def test_access_nested_map_exception(self, nested_map, path):
        """A tests for in valid keys"""
        with self.assertRaises(KeyError, msg=path):
            access_nested_map(nested_map, path)