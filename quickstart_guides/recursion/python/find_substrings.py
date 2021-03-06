"""
Title: Find substrings

Problem:
    Given a string, we have to find out all subsequences of it. A String is a
    subsequence of a given String, that is generated by deleting some character
    of a given string without changing its order.

Execution: python find_substrings.py
"""
from typing import List
import unittest


def find_substrings(test_str: str) -> List[str]:
    """Find substrings solution."""
    return [
        test_str[i:j]
        for i in range(len(test_str))
        for j in range(i + 1, len(test_str) + 1)
    ]


class TestFindSubstrings(unittest.TestCase):
    """Unit tests for interleaving_strings."""

    def test_1(self):
        expected_out = ["B", "By", "Byt", "Byte", "y", "yt", "yte", "t", "te", "e"]
        self.assertEqual(find_substrings("Byte"), expected_out)


if __name__ == "__main__":
    unittest.main()
