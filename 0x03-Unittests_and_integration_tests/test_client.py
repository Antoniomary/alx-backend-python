#!/usr/bin/env python3
"""
unit test for client
"""
from client import (
        GithubOrgClient
)
from parameterized import parameterized
from unittest.mock import patch, PropertyMock
import unittest
import utils


class TestGithubOrgClient(unittest.TestCase):
    """test cases
    """
    @parameterized.expand([
            ('google', {'url': 'https://api.github.com/orgs/google'}),
            ('abc', {'url': 'https://api.github.com/orgs/abc'})
    ])
    @patch("utils.requests.get")
    def test_org(self, org_name: str, expected: dict, mock_get):
        """tests the return value of GithubOrgClient.org
        """
        mock_get.return_value.json.return_value = expected

        obj = GithubOrgClient(org_name)

        result1 = obj.org
        result2 = obj.org

        self.assertEqual(result1, expected)
        self.assertEqual(result2, expected)

        mock_get.assert_called_with('https://api.github.com/orgs/' + org_name)
        mock_get.assert_called_once()

    def test_public_repos_url(self):
        """tests the result of _public_repos_url
        """
        with patch('utils.requests.get') as mock_get:
            mock_get.return_value.json.return_value = {"test": "mock"}

            obj = GithubOrgClient("test")
            result = obj.org["test"]
            assert result == "mock"

    @patch("client.get_json")
    def test_public_repos(self, mock_get_json):
        """tests the result of GithubOrgClient.public_repos
        """
        test_payload = {
            'repos_url': 'https://api.github.com/orgs/biz',
            'repos': [
                {
                    'id': 1,
                    'name': 'repo one',
                },
                {
                    'id': 2,
                    'name': 'repo two',
                },
            ]
        }

        mock_get_json.return_value = test_payload['repos']

        with patch('client.GithubOrgClient._public_repos_url',
                   new_callable=PropertyMock) as mock_repos:
            mock_repos.return_value = test_payload["repos"]
            obj = GithubOrgClient('biz')
            result = obj.public_repos()
            assert result == ['repo one', 'repo two']

            mock_repos.assert_called_once()

        mock_get_json.assert_called_once()


if __name__ == "__main__":
    unittest.main()
