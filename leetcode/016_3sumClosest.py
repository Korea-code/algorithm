class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:

        closest = nums[0] + nums[1] + nums[2]
        nums.sort()
        for i, num in enumerate(nums):
            i += 1
            j = len(nums) - 1
            while i < j:
                res = num + nums[i] + nums[j]
                if abs(target - res) < abs(target - closest):
                    closest = res
                if res < target:
                    i += 1
                else:
                    j -= 1
        return closest
