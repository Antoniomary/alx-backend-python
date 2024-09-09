#!/usr/bin/env python3
"""
unit test for client
"""
from client import (
        GithubOrgClient
)
from parameterized import parameterized
from unittest.mock import patch
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


if __name__ == "__main__":
    unittest.main()
