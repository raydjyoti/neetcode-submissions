class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
       # "AABABBA", k = 2
       # Keep a track of the most common word in a window
       # Keep expanding right window until k > 0
       # When k == 0, contract the left window, recheck the most common word
       # In the AABABBA example, new window after left contraction is ABABB.
       # B:3, A:2, B is the highest freq letter.
       # Total letter count == 5; totalCount - wordCount of most common == 3.
       # Ca veut dire, we have to  replace 2 letters.
       # Since k == 2, it's valid.
       # Expand the window to the right, new window becomes ABABBA. A:3, B:3
       # Most common letter, keep it A. totalCount - wordCount of most common - 6-3 == 3.
       # That means we need to replace 3 letters, not possible with k==2.
       # Hence contract the window from the left UNTIL wordCount-wordCount of most common <=k.


       # How do we keep track of the most common letter + its frequence in a window in O(1)?

        freqCount = dict();
        mostFreq = 0;
        output = 0;

        left = 0;
        right = 0;

        while left < len(s) and right < len(s):
            l = s[left];
            r = s[right];

            if r not in freqCount: freqCount[r] = 1;
            else: freqCount[r] += 1;

            if freqCount[r] > mostFreq:
                mostFreq = freqCount[r];

            windowLen = right-left+1;

            while (windowLen - mostFreq > k):
                freqCount[l] -= 1;
                left+=1;
                l = s[left];
                windowLen = right-left+1;

            right+=1
            output = max(output, right-left);

        return output 

                

