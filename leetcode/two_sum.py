from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        k = 1
        for i in range(len(nums)-1):
            if nums[i] + nums[k] == target:
                return nums.index(nums[i]), nums.index(nums[k])
            else:
                k += 1


nums = [2,7,11,15]
target = 9

Solution.twoSum(Solution, nums, target)
print(Solution.twoSum(Solution,nums, target))