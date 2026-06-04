class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:

        if len(s1) > len(s2): return False;

        bit1 = [0]*26;
        bit2 = [0]*26;

        for s in s1:
            ind = ord(s) - ord("a");
            bit1[ind] = bit1[ind] + 1;

        left = 0;
        right = 0;

        while right < len(s2):
            currLen = right-left;

            while currLen < len(s1):
                curr = s2[right];
                ind = ord(curr) - ord("a");
                bit2[ind] = bit2[ind] + 1;
                right+=1;
                currLen = right-left;

            if bit1 == bit2: return True;

            indL = ord(s2[left]) - ord("a");
            bit2[indL] -= 1;

            left += 1;


        return False;