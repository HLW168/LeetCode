class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        ans = 0
        # 利用雙指針找，從最右和最左往中間找
        left = 0
        right = len(height) - 1
        
        while left < right:
            ans = max(ans, min(height[left], height[right])*(right-left))
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1
        return ans
        
