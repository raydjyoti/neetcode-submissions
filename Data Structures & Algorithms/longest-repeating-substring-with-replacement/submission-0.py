class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        # hS = highest S, rS = rest of S's
        # Logic - In a window, find the highest occuring "s"
        # Any other "s", should be replaced
        # Total count - hS = rS
        # If, rS > k, means: we can't replace chars anymore..
        # Shift left + 1, right + 1
        # Only shifting left won't matter, since it's a smaller window

        store = {}
        left = 0
        right = 0
        maxSubStr = 0

        while right < len(s):
            curr = s[right]
            if (curr in store): store[curr] += 1
            else: store[curr] = 1

            totalCount = 0
            maxCount = 0

            for key in store:
                count = store[key]
                if count > maxCount: maxCount = count
                totalCount += count

            restCount = totalCount - maxCount

            if (restCount <= k):
                maxSubStr = totalCount
                # Extend window to right
                right+=1
            else:
                #Extend window from left & right
                right+=1
                leftS = s[left]
                store[leftS] -= 1
                left+=1

        return maxSubStr