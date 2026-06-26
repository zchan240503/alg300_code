class Solution:
    def isValid(self, s: str) -> bool:
        check_map = {
            "}": "{",
            ")": "(",
            "]" : "["
        }
        stack = []
        for char in s:
            if char in check_map:
                temp = stack.pop() if stack else '#'
                if check_map[char] != temp:
                    return False
            else :
                stack.append(char)
        return len(stack) == 0

               
a = Solution()
print(a.isValid('()[]{}'))