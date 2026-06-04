

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if (len(s) == 0): return 0
        # Check if you encountered something before
        # We need O(1) check - we need map/object
        # {p:0, w:1}, w index 2, {p: 0, w:2}, left = 2
        # {p:0, w:2, k:3}
        # {p:0, w:2, k:3, e:4}, left 2
        # {p:0, k:3, e:4, w:5}, left: 3

        left = 0
        store = {}
        maxLen = 1

        for i in range(len(s)):
            st = s[i]
            if (st not in store):
                store[st] = i
            else:
                # Check if prev st already behind left
                prevInd = store[st]

                if (prevInd >= left): left = prevInd+1
                store[st] = i

            subLen = (i-left)+1
            if (subLen > maxLen): maxLen = subLen

        return maxLen

