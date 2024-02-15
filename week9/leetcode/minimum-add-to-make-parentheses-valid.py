class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        stack=[]
        invalid=0
        for par in s:
            if par==")" and stack:
                stack.pop()
            elif par==")":
                invalid+=1
            else:
                stack.append(par)
        return len(stack) + invalid
        