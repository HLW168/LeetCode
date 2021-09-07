class Solution:
    def search(self, nums: List[int], target: int) -> int:
        
        # edge case
        if len(nums) == 0: return -1
        
        # two pointers
        l = 0
        r = len(nums) - 1
        
        # 分兩邊討論
        while l <= r:
            k = (l + r)//2
            # 剛好中間
            if target == nums[k]: 
                return k
           
            else:
                # 左半部 - 討論 k 的位置
                if nums[k] >= nums[l]:
                    # 左半部 - 討論 target 的位置 - 最左邊的情況
                    if target >= nums[l] and nums[k] > target: 
                        r = k-1
                    else: 
                        l = k + 1
                # 右半部 - 討論 k 的位置
                else:
                    # 右半部 - 討論 target 的位置 - 最右邊的情況
                    if target < nums[l] and target > nums[k]: 
                        l = k + 1
                    else:
                        r = k - 1
        return -1
