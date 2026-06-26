
class solution:
    def threeSumClosest(self, nums: list[int], target: int) -> int :
        end_sum = nums[0] + nums[1] + nums[2]
        nums.sort()
        for i in range(len(nums)-2):
            left = i+1
            right = len(nums)-1
            while left < right:
                sum = nums[i] + nums[left] + nums[right]
                if sum == target:
                    return sum
                elif sum > target:
                    right -= 1
                else :
                    left += 1
                if abs(target - end_sum) > abs(target - sum):
                    end_sum = sum
        return end_sum
if __name__ == '__main__':
    sol = solution()
    a = sol.threeSumClosest(nums = [-1,2,1,-4], target=1)
    print(a)
          
        