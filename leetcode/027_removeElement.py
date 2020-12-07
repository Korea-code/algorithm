class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        length = len(nums)
        j = 0
        for i in range(length):
            if nums[j] == val:
                length -= 1
                nums[j] = nums[length]
                j -= 1
            j += 1
        return length
