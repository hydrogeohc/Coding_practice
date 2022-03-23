class Solution(object):
    def toGoatLatin(self, sentence):
        """
        :type sentence: str
        :rtype: str
        """
        count = 0
        res = []
        for w in sentence.split():
            count += 1
            if w[0].lower() in ['a', 'e', 'i', 'o', 'u']:
                res.append(w+"ma"+'a'*count)
            else:
                res.append(w[1:]+w[0]+"ma"+'a'*count)
        return " ".join(res)
