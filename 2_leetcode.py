class Solution(object):
    def addTwoNumbers(self, l1, l2):
        ans = ListNode()
        carry = 0
        curr = ans
        curr_l1 = l1
        curr_l2 = l2
        while True:
            if curr_l1 is None:
                curr_l1 = ListNode()
            if curr_l2 is None:
                curr_l2 = ListNode()

            s = curr_l1.val + curr_l2.val + carry
            curr_val = s % 10
            carry = s / 10
            curr.val = curr_val
            
            curr_l1, curr_l2 = curr_l1.next, curr_l2.next
            if curr_l1 is None and curr_l2 is None and carry == 0:
                return ans
            curr.next = ListNode()
            curr = curr.next
                
