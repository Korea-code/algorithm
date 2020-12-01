class Solution:
    def isValid(self, s: str) -> bool:
        stack = [""]
        if len(s) == 0:
            return True
        stack.append(s[0])
        for l in s[1::]:
            if stack[-1] == "(" and l == ")" or stack[-1] == "{" and l == "}" or stack[-1] == "[" and l == "]":
                stack.pop()
            else:
                stack.append(l)

        if len(stack) == 1:
            return True
        else:
            return False
