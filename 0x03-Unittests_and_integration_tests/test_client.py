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
            mock_repos_url.return_value = "https://api.github.com/orgs/google/repos"
            new_class = GithubOrgClient('google')
            self.assertEqual(new_class._public_repos_url, "https://api.github.com/orgs/google/repos")

    @patch('client.get_json')
    def test_public_repos(self, mocked_get_json):
        """A function to test the public_repos method"""
        mock = Mock()
        mock.json.return_value = ['strings']
        mocked_get_json.return_value = mock
        new_class = GithubOrgClient('google')
        # patch to mock the public_repos_url"""
        with patch(
            'client.GithubOrgClient._public_repos_url',
            new_callable=PropertyMock
        ) as mock_repos_url:
            mock_repos_url.return_value = "string"
            self.assertEqual(new_class._public_repos_url, "string")
            mock_repos_url.assert_called_once()
        new_class.public_repos
        # mocked_get_json.assert_called_once()