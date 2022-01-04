# Time:  O(n)
# Space: O(n)

class Solution(object):
    def decodeString(self, s):
        """
        :type s: str
        :rtype: str
        """
        n, curr, nums, strs = 0, [], [], []
        for c in s:
            if c.isdigit():
                n = n*10 + ord(c)-ord('0')
            elif c.isalpha():
                curr.append(c)
            elif c == '[':
                nums.append(n)
                strs.append(curr)
                n, curr = 0, []
            elif c == ']':
                strs[-1].extend(curr*nums.pop())
                curr = strs.pop()
        return "".join(curr)

## stack
class Solution(object):
    def decodeString(self, s):
        """
        :type s: str
        :rtype: str
        """
        stack = []
        
        for c in s:
            if c != ']':
                stack.append(c)
                continue
            
            strs = []
            while stack and stack[-1] != '[':
                strs.append(stack.pop())
                
            stack.pop()
            
            repeats = 0
            base = 1
            while stack and stack[-1].isdigit():
                repeats += (ord(stack.pop()) - ord('0')) * base
                base *= 10
            stack.append(''.join(reversed(strs)) * repeats)
            
        return ''.join(stack)