class Solution:
    def removeDuplicates(self, nums) -> int:
        cur = 0
        next = cur+1
        while(next < len(nums)):
            if(nums[cur] == nums[next] and nums[cur] != '_'):
                nums[next] = "_"
                next+=1
            else:
                cur = next
                next = cur + 1
        count = 0
        for i in range(len(nums)):
            if nums[i]!='_':
                temp = nums[i]
                nums[i] = nums[count]
                nums[count] = temp
                count += 1
        return nums
a = Solution()
b = a.removeDuplicates([0,0,1,1,1,2,2,3,3,4])
print(b)