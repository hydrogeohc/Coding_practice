class Solution(object):
    def uncommonFromSentences(self, s1, s2):
        """
        :type s1: str
        :type s2: str
        :rtype: List[str]
        """
        c = collections.Counter((s1 + " " + s2).split())
        return [w for w in c if c[w] == 1]
