#!/usr/bin/env python3
"""
unit test for utils.access_nested_map
"""
from parameterized import parameterized
from typing import (
        Mapping,
        Sequence
)
import unittest
import utils


class TestAccessNestedMap(unittest.TestCase):
    """test for utils.access_nested_map
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


if __name__ == "__main__":
    unittest.main()
