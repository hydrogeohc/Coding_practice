class Solution:
    def isMonotonic(self, A):
        if len(A) == 1:
            return True
        increasing = True if A[-1] > A[0] else False
        prev = A[0]
        if increasing:
            for i in range(1, len(A)):
                if A[i] < prev:
                    return False
                prev = A[i]
        else:
            for i in range(1, len(A)):
                if A[i] > prev:
                    return False
                prev = A[i]
        return True
