class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        length = 0
        if not len(nums):
            return length
        for num in nums[1:]:
            if nums[length] != num:
                length += 1
                nums[length] = num
        return length + 1
