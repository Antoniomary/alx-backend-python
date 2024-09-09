#!/usr/bin/env python3
"""
unit test for utils.access_nested_map
"""
from parameterized import parameterized
from typing import (
        Mapping,
        Sequence
)
from unittest.mock import patch
import unittest
import utils


class TestAccessNestedMap(unittest.TestCase):
    """test cases
    """
    @parameterized.expand([
            ({"a": 1}, ("a",), 1),
            ({"a": {"b": 2}}, ("a",), {"b": 2}),
            ({"a": {"b": 2}}, ("a", "b"), 2)
    ])
    def test_access_nested_map(self,
                               nested_map: Mapping, path: Sequence,
                               expected):
        """test the return value of utils.access_nested_map
        """
        self.assertEqual(utils.access_nested_map(nested_map, path), expected)

    @parameterized.expand([
            ({}, ("a",), "KeyError: 'a'"),
            ({"a": 1}, ("a", "b"), "KeyError: 'b'")
    ])
    def test_access_nested_map_exception(self,
                                         nested_map: Mapping, path: Sequence,
                                         expected):
        """tests for exceptions in utils.access_nested_map
        """
        with self.assertRaises(KeyError) as cm:
            utils.access_nested_map(nested_map, path)
            self.assertEqual(cm.exception, expected)


class TestGetJson(unittest.TestCase):
    """test cases
    """
    @parameterized.expand([
            ("http://example.com", {"payload": True}),
            ("http://holberton.io", {"payload": False})
    ])
    @patch("utils.requests.get")
    def test_get_json(self, test_url: str, test_payload: dict, mock_get):
        """test that utils.get_json returns the expected result
        """
        mock_get.return_value.json.return_value = test_payload
        result = utils.get_json(test_url)
        self.assertEqual(result, test_payload)
        mock_get.assert_called_once_with(test_url)


if __name__ == "__main__":
    unittest.main()
