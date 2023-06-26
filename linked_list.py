# -- coding: utf-8 --
# @Time : 2023/6/25
# @Author : ykk648
# @Project : https://github.com/ykk648/leetcode_useless
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:

    # 141 环形链表
    def cycle_judge(self, head):
        # 2节点以下无法成环
        if not head or not head.next:
            return False
        fast, slow = head.next, head
        while fast != slow:
            if not fast or not fast.next:
                return False
            fast = fast.next.next
            slow = slow.next
        return True

    # 142 环形链表II ，求环形入口
    def cycle_entry(self, head):
        fast, slow = head, head
        while True:
            if not fast or not fast.next:
                return
            fast, slow = fast.next.next, slow.next
            if fast == slow:
                break
        # 重合后head入环的距离等于slow到环形入口的距离
        fast = head
        while fast != slow:
            fast, slow = fast.next, slow.next
        return fast

    # 206 反转链表
    def reverse(self, head):
        cur, pre = head, None
        while cur:
            temp = cur.next
            cur.next = pre
            pre = cur
            cur = temp
        return pre

    # 25 K个一组翻转列表
    def reverse_partial(self, start, end):
        # 区域翻转(start-end之间的部分)
        cur, pre = start.next, start
        dummy = cur
        while cur != end:
            temp = cur.next
            cur.next = pre
            pre = cur
            cur = temp
        start.next = pre
        dummy.next = cur
        return pre

    def reverse_k_group(self, head, k):
        if not head or k < 2:
            return head
        # 防止head被改变
        dummy = ListNode(0)
        dummy.next = head
        # 开始遍历
        start = dummy
        end = head
        count = 0
        while end:
            count += 1
            if count % k == 0:
                start = self.reverse_partial(start, end.next)
                end = start.next
            else:
                end = end.next
        return dummy.next

    # 21 合并两个有序链表 （递归）
    def merge_list_node(self, head1, head2):
        if not head1:
            return head2
        if not head2:
            return head1
        if head1.val < head2.val:
            head1.next = self.merge_list_node(head1.next, head2)
            return head1
        else:
            head2.next = self.merge_list_node(head1, head2.next)
            return head2

