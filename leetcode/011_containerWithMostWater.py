class Solution:
    def maxArea(self, height: List[int]) -> int:
        end = len(height) - 1
        volume, maxVolume = 0, 0
        start = 0
        while start < end:
            if height[start] > height[end]:
                volume = (end - start) * height[end]
            else:
                volume = (end - start) * height[start]
            if maxVolume < volume:
                maxVolume = volume
            if height[start] < height[end]:
                start += 1
            else:
                end -= 1
        return maxVolume
