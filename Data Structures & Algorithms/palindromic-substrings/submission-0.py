class Solution:
    def countSubstrings(self, s: str) -> int:
        self.seen = set()
        self.output = 0

        def isPal(left, right):

            if left < 0: return
            if right >= len(s): return

            while left >= 0 and right < len(s):
                leftVal = s[left]
                rightVal = s[right]

                if leftVal is not rightVal: return

                if (left, right) not in self.seen:
                    self.output += 1
                    self.seen.add((left,right))

                left -= 1
                right += 1

            return

        for i in range(len(s)):
            isPal(i, i)
            isPal(i, i+1)

        return self.output
