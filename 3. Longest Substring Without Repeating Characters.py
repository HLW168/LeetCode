class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        start = 0
        maxLength = 0
        usedChar = {}
        
        for i in range(len(s)):
            # start 左邊重複的不用管
            if s[i] in usedChar and start <= usedChar[s[i]]:
                # start 跳過重複的
                start = usedChar[s[i]]+1
            else:
                # i - start + 1 計算沒有重複的長度
                maxLength = max(maxLength, i-start+1)
            
            usedChar[s[i]] = i
            
        return maxLength
