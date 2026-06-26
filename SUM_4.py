class Solution:
    def fourSum(self, nums, target: int):
        nums.sort()
        resuilt = []
        for i in range(len(nums)):
            for j in range(i+1, len(nums) - 2):
                if j > i+1 and nums[j] == nums[j-1]:
                    continue
                left = j+1
                right = len(nums)-1
                while left < right:
                    tmp = nums[i] + nums[j] + nums[left] + nums[right]
                    if tmp > target:
                        right-=1
                    elif tmp < target:
                        left += 1
                    else :
                        res = [nums[i], nums[j], nums[left], nums[right]]
                        if res not in resuilt:
                            resuilt.append(res)
                        while left < right and nums[left] == nums[left+1]:
                            left+=1
                        while left < right and nums[right] == nums[right-1]:
                            right -= 1
                        left+=1  
                        right-=1         
        return resuilt
a = Solution()
res = a.fourSum(nums=[-3,-2,-1,0,0,1,2,3], target=0)
print(res)
            