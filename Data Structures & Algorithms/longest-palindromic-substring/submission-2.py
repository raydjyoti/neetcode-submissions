class Solution:
    def longestPalindrome(self, s: str) -> str:

        self.output = ""

        def isPalindrome(l, r):

            while l >= 0 and r < len(s):
                left = s[l]
                right = s[r]

                if left is not right: return

                if r-l+1 > len(self.output):
                    self.output = s[l:r+1]
                
                l -= 1
                r += 1

        
        for i in range(len(s)):
            isPalindrome(i, i)
            isPalindrome(i, i+1)

        return self.output


