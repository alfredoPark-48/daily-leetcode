# Given an array of strings strs, group the anagrams together. You can return the answer in any order.
# An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.

# Example 1:
# Input: strs = ["eat","tea","tan","ate","nat","bat"]
# Output: [["bat"],["nat","tan"],["ate","eat","tea"]]

# Example 2:
# Input: strs = [""]
# Output: [[""]]

# Example 3:
# Input: strs = ["a"]
# Output: [["a"]]

import unittest


def group_anagrams(strs):
    
    pass


class GroupAnagramsTest(unittest.TestCase):
    def test_case1(self):
        self.assertEqual(
            group_anagrams(
                ["eat", "tea", "tan", "ate", "nat", "bat"],
                [["bat"], ["nat", "tan"], ["ate", "eat", "tea"]],
                "Should be a list of anagrams grouped together",
            )
        )

    def test_case2(self):
        self.assertEqual(
            [""], [[""]], "Should be a list with a list with an empty string"
        )

    def test_case3(self):
        self.assertEqual(
            ["a"], [["a"]], "Should be a list with a list of a single character"
        )

    def test_case4(self):
        self.assertEqual(
            group_anagrams(["cat", "act", "tac", "dog", "god"]),
            [["cat", "act", "tac"], ["dog", "god"]],
            "Should be a list with anagrams grouped together",
        )

    def test_case5(self):
        self.assertEqual(
            group_anagrams(["abc", "def", "cba", "fed"]),
            [["abc", "cba"], ["def", "fed"]],
            "Should be a list with anagrams grouped together",
        )

    def test_case6(self):
        self.assertEqual(
            group_anagrams(["abcd", "dcba", "efgh", "hgfe"]),
            [["abcd", "dcba"], ["efgh", "hgfe"]],
            "Should be a list with anagrams grouped together",
        )

    def test_case7(self):
        self.assertEqual(
            group_anagrams(["listen", "silent", "elbow", "below"]),
            [["listen", "silent"], ["elbow", "below"]],
            "Should be a list with anagrams grouped together",
        )

    def test_case8(self):
        self.assertEqual(
            group_anagrams(["abcd", "efgh", "ijkl", "mnop"]),
            [["abcd"], ["efgh"], ["ijkl"], ["mnop"]],
            "Should be a list with each word in its own group",
        )

    def test_case9(self):
        self.assertEqual(
            group_anagrams(["race", "care", "acre", "rare"]),
            [["race", "care", "acre"], ["rare"]],
            "Should be a list with anagrams grouped together",
        )

    def test_case10(self):
        self.assertEqual(
            group_anagrams(["cat", "dog", "car", "god", "arc"]),
            [["cat"], ["dog", "god"], ["car", "arc"]],
            "Should be a list with anagrams grouped together",
        )


if __name__ == "__main__":
    unittest.main()
