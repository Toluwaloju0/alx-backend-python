#!/usr/bin/env python3
"""A module to test the utils packsge"""

import functools
from parameterized import parameterized
import requests
import unittest
from unittest.mock import patch, Mock
from utils import access_nested_map, get_json, memoize


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


class TestGetJson(unittest.TestCase):
    """The class to test the get json of the utils module"""

    @parameterized.expand([
        ("http://example.com", {"payload": True}),
        ("http://holberton.io", {"payload": False})
    ])
    def test_get_json(self, test_url, test_payload):
        """A function to test the get json function of utils"""
        with patch('requests.get') as mocked_get:
            mock_result = Mock()
            mock_result.json.return_value = test_payload
            mocked_get.return_value = mock_result
            self.assertEqual(get_json(test_url), test_payload)


class TestMemoize(unittest.TestCase):
    """To test the memoize class"""

    def test_memoize(self):
        """To test the memoize func in utils"""
        class TestClass:
            def a_method(self):
                return 42

            @memoize
            def a_property(self):
                return self.a_method()
            
            @patch('self.a_method')
            def test_a_property(self, mocked_a_method):
                """To test that a method is called once"""

                self.a_property()
                self.a_property()

                mocked_a_method.assert_called_once