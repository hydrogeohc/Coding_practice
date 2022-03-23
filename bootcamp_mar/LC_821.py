class Solution(object):
    def shortestToChar(self, s, c):
        """
        :type s: str
        :type c: str
        :rtype: List[int]
        """
        l = [0] * len(s)
        prev = None
        for i, x in enumerate(s):
            if x == c:

		
                start = 0 if prev is None else (i + prev) // 2 + 1
                l[start:i + 1] = range(i - start, -1, -1)

                prev = i
            elif prev is not None:
                l[i] = i - prev
        return l
