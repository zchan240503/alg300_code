class Solution:
    def letterCombinations(self, digits: str):
        if not digits:
            return []
        lb = {
            2 : 'abc',
            3 : 'def',
            4 : 'ghi',
            5 : 'jkl',
            6 : 'mno',
            7 : 'pqrs',
            8 : 'tuv',
            9 : 'wxyz',
        }
        resuilt = []
        if len(digits) < 2:
            for i in range(len(lb[int(digits[0])])):
                resuilt.append(lb[int(digits[0])][i])
        elif len(digits) == 2:
            for i in range(len(lb[int(digits[0])])):
                for j in range(len(lb[int(digits[1])])):
                    resuilt.append(lb[int(digits[0])][i] + lb[int(digits[1])][j])
        else :
            size = len(digits)
            temp_left = []
            temp_right = []
            for i in range(len(lb[int(digits[0])])):
                for j in range(len(lb[int(digits[1])])):
                    temp_left.append(lb[int(digits[0])][i] + lb[int(digits[1])][j])
            if size == 3 :
                for i in range(len(lb[int(digits[2])])):
                    temp_right.append(lb[int(digits[2])][i])
            else :
                for i in range(len(lb[int(digits[2])])):
                    for j in range(len(lb[int(digits[3])])):
                        temp_right.append(lb[int(digits[2])][i] + lb[int(digits[3])][j])
            for i in range(len(temp_left)):
                for j in range(len(temp_right)):
                    resuilt.append(temp_left[i] + temp_right[j])
        return resuilt


a = Solution()
res = a.letterCombinations(digits='2345')
print(res)