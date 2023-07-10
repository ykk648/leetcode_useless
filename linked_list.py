# -- coding: utf-8 --
# @Time : 2023/6/25
# @Author : ykk648
# @Project : https://github.com/ykk648/leetcode_useless
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def reverse_partial(start, end):
    # 区域翻转(start-end之间的部分) 返回start-end区间中的头尾节点 inplace
    cur, pre = start.next, start
    dummy = cur
    while cur != end:
        temp = cur.next
        cur.next = pre
        pre = cur
        cur = temp
    start.next = pre
    dummy.next = cur
    return pre, dummy


def reverse_partial_count(start, count):
    # 从start处翻转count次， count = start-end+1与reverse_partial一致，返回start下一个节点
    cur, pre = start.next, start
    dummy = cur
    while count > 0:
        temp = cur.next
        cur.next = pre
        pre = cur
        cur = temp
        count -= 1
    start.next = pre
    dummy.next = cur
    return pre, dummy


class LinkReverse:
    # 206 反转链表
    def reverse(self, head):
        cur, pre = head, None
        while cur:
            temp = cur.next
            cur.next = pre
            pre = cur
            cur = temp
        return pre

    # 反转链表 复用写法
    def reverse_2(self, head):
        if not head:
            return head
        dummy = ListNode(0)
        dummy.next = head
        res, _ = reverse_partial(dummy, None)
        return res

    # 92 反转链表II
    def reverse_partial_from_head(self, head, left, right):
        if not head:
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
            if count < left:
                start = start.next
            else:
                _, _ = reverse_partial_count(start, right - left + 1)
                break
        return dummy.next

    # 25 K个一组翻转列表 复用写法
    def reverse_k_group(self, head, k):
        if not head or k == 1:
            return head
        dummy = ListNode(0)
        dummy.next = head

        start = dummy
        end = head
        count = 0
        while end:
            count += 1
            if count % k == 0:
                _, start = reverse_partial(start, end.next)
                end = start.next
            else:
                end = end.next
        return dummy.next


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

    # 23 合并K个有序链表 （merge 归并）
    def merge_k_list_node(self, list_nodes):
        if not list_nodes:
            return None

        def merge_sort(lists, l, r):
            if l == r:
                return lists[l]
            m = (l + r) // 2
            return self.merge_list_node(merge_sort(lists, l, m), merge_sort(lists, m + 1, r))

        return merge_sort(list_nodes, 0, len(list_nodes) - 1)

    # 328 奇偶链表
    def odd_even_list(self, head):
        if not head:
            return head
        odd = head
        even = dummy = head.next
        while odd.next and even.next:
            odd.next = odd.next.next
            even.next = even.next.next
            odd = odd.next
            even = even.next
        odd.next = dummy
        return head

    # 160 相交链表 (拼接链表
    def cross_list(self, head1, head2):
        p1, p2 = head1, head2
        while p1 != p2:
            p1 = p1.next if p1 else head2
            p2 = p2.next if p2 else head1
        return p1

    # 19 删除链表的倒数N个节点 ( double p
    def remove_reverse_k_node(self, head, n):
        p1 = p2 = dummy = ListNode(next=head)
        for _ in range(n):
            p2 = p2.next
        while p2.next:
            p1 = p1.next
            p2 = p2.next
        p1.next = p1.next.next
        return dummy
