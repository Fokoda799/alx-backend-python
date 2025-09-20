#!/usr/bin/env python3
"""
Unit tests for utils.access_nested_map, utils.get_json,
and utils.memoize.
"""

import unittest
from unittest.mock import patch
from utils import access_nested_map, get_json, memoize
from parameterized import parameterized


class TestAccessNestedMap(unittest.TestCase):
    """Unit tests for the access_nested_map function."""

    @parameterized.expand([
        ({"a": 1}, ("a",), 1),
        ({"a": {"b": 2}}, ("a",), {"b": 2}),
        ({"a": {"b": 2}}, ("a", "b"), 2),
    ])
    def test_access_nested_map(self, nested_map, path, expected):
        """Test access_nested_map with valid inputs."""
        self.assertEqual(
            access_nested_map(nested_map, path),
            expected,
            f"Expected {expected} for path {path}, but got different result."
        )

    @parameterized.expand([
        ({}, ("a",), KeyError),
        ({"a": 1}, ("a", "b"), KeyError),
    ])
    def test_access_nested_map_exception(
        self, nested_map, path, expected_exception
    ):
        """Test that access_nested_map raises the correct exceptions."""
        with self.assertRaises(expected_exception):
            access_nested_map(nested_map, path)


class TestGetJson(unittest.TestCase):
    """Unit tests for the get_json function."""

    @patch("utils.requests.get")
    def test_get_json(self, mock_get):
        """Test get_json with a mocked requests.get."""
        mock_get.return_value.json.return_value = {"status": "ok"}

        result = get_json("http://fakeurl.com")

        self.assertEqual(
            result,
            {"status": "ok"},
            "get_json did not return the expected dictionary."
        )
        mock_get.assert_called_once_with("http://fakeurl.com")


class TestMemoize(unittest.TestCase):
    """Unit tests for the memoize decorator."""

    def test_memoize(self):
        """Test that memoize caches the result of a method."""

        class TestClass:
            """Helper class to test the memoize decorator."""

            def a_method(self):
                """Return a fixed value (42)."""
                return 42

            @memoize
            def a_property(self):
                """Return the result of a_method (memoized)."""
                return self.a_method()

        test_obj = TestClass()

        with patch.object(
            TestClass,
            "a_method",
            return_value=42
        ) as mock_a_method:
            # First access should call a_method
            result1 = test_obj.a_property
            self.assertEqual(result1, 42)

            # Second access should use cached value
            result2 = test_obj.a_property
            self.assertEqual(result2, 42)

            # Ensure a_method was called only once
            mock_a_method.assert_called_once()


if __name__ == "__main__":
    unittest.main()
