class Solution:
    def convert(self, s: str, numRows: int) -> str:
        buckets = []
        indices = []
        for i in range(numRows):
            buckets.append([] * numRows)
            indices.append(i)

        if numRows > 2:
            indices = [*indices, *reversed(indices[1:-1])]

        for i in range(len(s)):
            index = indices[i % len(indices)]
            buckets[index].append(s[i])

        return "".join([char for bucket in buckets for char in bucket])
