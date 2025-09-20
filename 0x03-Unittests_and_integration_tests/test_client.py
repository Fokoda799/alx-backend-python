#!/usr/bin/env python3
"""
Module: test_github_org_client.py
--------------------------------
This module contains unit and integration tests for the
`GithubOrgClient` class. It uses the `unittest` framework,
along with `unittest.mock` and `parameterized`, to test the
functionality of fetching and processing GitHub organization
data.
"""

import unittest
from unittest.mock import patch, PropertyMock, MagicMock
from parameterized import parameterized, parameterized_class
from client import GithubOrgClient
from fixtures import TEST_PAYLOAD
import utils


class TestGithubOrgClient(unittest.TestCase):
    """
    Unit test class for `GithubOrgClient`.
    Tests individual methods and properties of the
    `GithubOrgClient` class.
    """

    @parameterized.expand([
        ("google",),
        ("abc",),
    ])
    @patch('client.get_json')
    def test_org(self, org_name, mock_get_json):
        """
        Test that `GithubOrgClient.org` returns the correct
        organization data.
        """
        expected_org_data = {"login": org_name, "id": 12345}
        mock_get_json.return_value = expected_org_data
        client = GithubOrgClient(org_name)
        result = client.org
        expected_url = f"https://api.github.com/orgs/{org_name}"
        mock_get_json.assert_called_once_with(expected_url)
        self.assertEqual(result, expected_org_data)

    def test_public_repos_url(self):
        """
        Test that `_public_repos_url` returns the expected URL
        for public repositories.
        """
        known_payload = {
            "login": "test_org",
            "id": 12345,
            "repos_url": "https://api.github.com/orgs/test_org/repos"
        }
        with patch.object(
            GithubOrgClient,
            'org',
            new_callable=PropertyMock
        ) as mock_org:
            mock_org.return_value = known_payload
            client = GithubOrgClient("test_org")
            result = client._public_repos_url
            expected_url = known_payload["repos_url"]
            self.assertEqual(result, expected_url)

    @patch("client.get_json")
    def test_public_repos(self, mock_get_json):
        """
        Test that `public_repos` returns the correct list of
        repository names.
        """
        payload = [
            {"name": "repo1"},
            {"name": "repo2"}
        ]
        mock_get_json.return_value = payload
        with patch.object(
            GithubOrgClient,
            "_public_repos_url",
            new_callable=PropertyMock
        ) as mock_pru:
            mock_pru.return_value = (
                "https://api.github.com/orgs/test_org/repos"
            )
            client = GithubOrgClient("test_org")
            result = client.public_repos()
            self.assertEqual(result, ["repo1", "repo2"])
            mock_get_json.assert_called_once_with(
                "https://api.github.com/orgs/test_org/repos"
            )
            mock_pru.assert_called_once()

    @parameterized.expand([
        ({"license": {"key": "my_license"}}, "my_license", True),
        ({"license": {"key": "other_license"}}, "my_license", False),
    ])
    def test_has_license(self, repo, license_key, expected):
        """
        Test the static method `has_license` to check if a
        repository has a specific license.
        """
        self.assertEqual(
            GithubOrgClient.has_license(repo, license_key),
            expected
        )


test_payload = TEST_PAYLOAD[0]


@parameterized_class([{
    "org_payload": test_payload[0],
    "repos_payload": test_payload[1],
    "expected_repos": test_payload[2],
    "apache2_repos": test_payload[3],
}])
class TestIntegrationGithubOrgClient(unittest.TestCase):
    """
    Integration test class for `GithubOrgClient.public_repos`.
    Tests the interaction between methods and external API calls.
    """

    @classmethod
    def setUpClass(cls):
        """Patch `requests.get` to return predefined payloads."""
        cls.get_patcher = patch("utils.requests.get")
        mock_get = cls.get_patcher.start()

        def side_effect(url):
            mock_response = MagicMock()
            if url.endswith("orgs/google"):
                mock_response.json.return_value = cls.org_payload
            elif url.endswith("orgs/google/repos"):
                mock_response.json.return_value = cls.repos_payload
            return mock_response

        mock_get.side_effect = side_effect

    @classmethod
    def tearDownClass(cls):
        """Stop the patcher."""
        cls.get_patcher.stop()

    def test_public_repos(self):
        """Test that `public_repos` returns the expected list."""
        client = GithubOrgClient("google")
        self.assertEqual(client.public_repos(), self.expected_repos)

    def test_public_repos_with_license(self):
        """Test `public_repos` with a license filter."""
        client = GithubOrgClient("google")
        self.assertEqual(
            client.public_repos(license="apache-2.0"),
            self.apache2_repos
        )


if __name__ == "__main__":
    unittest.main()
