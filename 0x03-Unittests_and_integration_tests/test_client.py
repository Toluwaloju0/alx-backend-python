#!/usr/bin/env python3
"""A module to test the client module"""

import unittest
from client import GithubOrgClient
from parameterized import parameterized
from unittest.mock import Mock, patch, PropertyMock


class TestGithubOrgClient(unittest.TestCase):
    """A class to test the GithubOrgClient class"""

    @parameterized.expand([
        ('google'),
        ('abc')
    ])
    def test_org(self, org_name):
        with patch('utils.get_json') as get_json:
            get_json.called_once_with(org_name)

    def test_public_repos_url(self):
        """To test a property mock and test the _public_repos_url"""
        with patch(
            'client.GithubOrgClient._public_repos_url',
            new_callable=PropertyMock
        ) as mock_repos_url:
            mock_repos_url.return_value = 'Url_string'
