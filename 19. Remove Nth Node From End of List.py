# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        if head is None: return head
        
        dummy = ListNode(-1, head)
        fast, slow, pre = dummy, dummy, dummy
        
        # 先讓 fast 走，跟 slow 保持 n-1 的距離
        while n-1:
            fast = fast.next
            n -= 1
        # 其他人可以走了
        while fast.next:
            fast = fast.next
            # 用 pre 紀錄 slow 走之前的位置
            pre =slow
            slow = slow.next
        pre.next = slow.next
        
        return dummy.next
