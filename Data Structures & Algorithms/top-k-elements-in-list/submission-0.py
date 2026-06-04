class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        store = dict()

        for n in nums:
            if n in store: store[n] += 1
            else: store[n] = 1


        # Python jargon

        return list(map(lambda x: x[0] ,sorted(store.items(), key=lambda x: x[1], reverse=True)))[0:k:1]