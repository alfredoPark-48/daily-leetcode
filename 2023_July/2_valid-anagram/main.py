# Given two strings s and t, return true if t is an anagram of s, and false otherwise.
# An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.

# Example 1:
# Input: s = "anagram", t = "nagaram"
# Output: true

# Example 2:
# Input: s = "rat", t = "car"
# Output: false

import unittest


def is_anagram(s, t):
    if len(s) != len(t):
        return False
    else:
        s_map = {}
        t_map = {}

        for i in range(len(s)):
            s_map[s[i]] = 1 + s_map.get(s[i], 0)
            t_map[t[i]] = 1 + t_map.get(t[i], 0)

        for char in s_map:
            if char not in t_map and s_map[char] != t_map[char]:
                return False

        return True


class IsAnagramTest(unittest.TestCase):
    def test_case1(self):
        self.assertEqual(is_anagram("anagram", "nagaram"), True, "Should be true")

    def test_case2(self):
        self.assertEqual(is_anagram("rat", "car"), False, "Should be false")

    def test_case3(self):
        self.assertEqual(is_anagram("listen", "silent"), True, "Should be true")

    def test_case4(self):
        self.assertEqual(is_anagram("hello", "world"), False, "Should be false")

    def test_case5(self):
        self.assertEqual(is_anagram("cinema", "iceman"), True, "Should be true")

    def test_case6(self):
        self.assertEqual(is_anagram("abcdefg", "gfedcba"), True, "Should be true")

    def test_case7(self):
        self.assertEqual(
            is_anagram("abcd", "abcd"), True, "Should be true"
        )  # Same string

    def test_case8(self):
        self.assertEqual(is_anagram("", ""), True, "Should be true")  # Empty strings

    def test_case9(self):
        self.assertEqual(
            is_anagram("abc", "abcd"), False, "Should be false"
        )  # Different lengths

    def test_case10(self):
        self.assertEqual(
            is_anagram("aab", "bba"), False, "Should be false"
        )  # Different frequency of characters


if __name__ == "__main__":
    unittest.main()
