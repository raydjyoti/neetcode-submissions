from collections import deque;

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        q = deque();
        store = set();
        output = float('-inf');

        if not s: return 0

        for i in s:
            
            
            if i in store:
                while len(q) > 0:
                    first = q.popleft();
                    store.remove(first);
                    if first == i: break
            
            q.append(i);
            output = max(output, len(q));
            store.add(i);

        return output;
            

