class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        res = []
        n = len(nums)
        #排序
        nums.sort()
        # 遍歷，且利用左右指針向中間指
        # 需跳過相同的數字，因為相同的數字組合只能出現一次
        for i in range(n):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            target = nums[i] * -1
            start = i + 1
            end = n - 1
            # 指針
            while start < end:
                if nums[start] + nums[end] == target:
                    res.append([nums[i], nums[start], nums[end]])
                    # start 向前走
                    start += 1
                    while start < end and nums[start] == nums[start-1]:
                        start += 1
                elif nums[start] + nums[end] < target:
                    start += 1
                else:
                    end -= 1
        return res
