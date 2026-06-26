class Solution:
    def generateParenthesis(self, n: int):
        resuilt = []
        def backtrack(curentstring, count_open, count_close):
            if len(curentstring) == n*2:
                resuilt.append(curentstring)
                return
            if count_open < n:
                backtrack(curentstring+'(', count_open+1, count_close)
            if count_close < count_open:
                backtrack(curentstring+')', count_open, count_close+1)
        backtrack("", 0, 0)
        return resuilt
a = Solution()
print(a.generateParenthesis(3))
            
