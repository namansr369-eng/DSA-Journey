#14 Largest Common Prefix

from typing import List


class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not all(strs):
            return ""
        smallest = min(strs, key=len)
        for i, char in enumerate(smallest):
            if not all( s[i]==char for s in strs):
                return smallest[:i]

        return smallest