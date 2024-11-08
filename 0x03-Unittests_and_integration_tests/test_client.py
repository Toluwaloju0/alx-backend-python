#!/usr/bin/env python3
"""A module to test the client module"""

import unittest
from client import GithubOrgClient
from parameterized import parameterized
from unittest.mock import patch


class TestGithubOrgClient(unittest.TestCase):
    """A class to test the GithubOrgClient class"""

    @parameterized.expand([
        ('google'),
        ('abc')
    ])
    def test_org(self, org_name):
        with patch('utils.get_json') as get_json:
            get_json.called_once_with(org_name)