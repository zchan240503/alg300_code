class Solution:
    def removeElement(self, nums, val: int) -> int:
        for i in range(len(nums)):
            if nums[i] == val:
                nums[i] = '_'
        print(nums)
        count = 0
        for i in range(len(nums)):
            if nums[i]!='_':
                temp = nums[i]
                nums[i] = nums[count]
                nums[count] = temp
                count += 1

        return count
a = Solution()
print(a.removeElement(nums = [0,1,2,2,3,0,4,2], val = 2))