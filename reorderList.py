# Definition for singly-linked list.
import math
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

    def __str__(self):
        n = self
        result = ""
        while n is not None:
            result += str(n.val) + "->"
            n = n.next
        result += "NIL"
        return result


class Solution:
    # @param A : head node of linked list
    # @return the head node in the linked list
    def reorderList(self, A):
        length, last = Solution.sizenlast(A)
        length += 1
        if length < 3:
            print(length)
            return A
        mid = math.floor(length/2)
        mid_node = A
        # find middle node
        # mid - 1 or mid
        # odd: mid
        # even: mid
        for i in range(0, mid):
            mid_node = mid_node.next
        prev_mid = mid_node
        mid_node = mid_node.next
        # odd : mid
        # even: mid -1
        if length % 2 == 0:
            mid -= 1
        #new_mid = self.rev(mid_node, mid)
        new_mid = self.revloop(mid_node, mid-1)
        prev_mid.next = None
        # odd: mid
        # even: mid-1
        Solution.weave(A, last, mid)
        # now last is middle
        # prev still one before it

    def rev(self, list, k):
        if k == 1:
            return list
        else:
            t = self.rev(list.next, k-1)
            list.next = None
            t.next = list
            return t.next

    def revloop(self, n, k):
        prev, n = n, n.next
        prev.next = None
        for i in range(0, k):
            tmp = n.next
            n.next = prev
            prev = n
            n = tmp

    def weave(head, mid, n):
        for i in range(0, n):
            tmp1 = head.next
            tmp2 = mid.next
            head.next = mid
            mid.next = tmp1
            head = tmp1
            mid = tmp2
        if mid is not None:
            head.next = mid


    def sizenlast(self):
        head = self
        length = 0
        while head.next is not None:
            head = head.next
            length += 1
        return length, head


if __name__ == "__main__":
    # execute only if run as a script
    sol = Solution()
    tmp = None
    list = [90, 94, 25, 51, 45, 29, 55, 63 ,48, 27, 72, 10, 36, 68, 16, 20, 31, 7, 95, 70, 89, 23, 22, 9, 74, 71, 35, 5, 80, 11, 49, 92, 69, 6, 37, 84, 78, 28, 43, 64, 96, 57, 83, 13, 73, 97, 75, 59, 53, 52, 19, 18, 98, 12, 81, 24, 15, 60, 79, 34, 1, 54, 93, 65, 44, 4, 87, 14, 67, 26, 30, 77, 58, 85, 33, 21, 46, 82, 76, 88, 66, 101, 61, 47, 8]
    list = list[::-1]
    for i in range(8, 0, -1):
    #for i in list:
        n = ListNode(i)
        n.next = tmp
        tmp = n
    tmp2 = tmp
    print(tmp)
    while tmp.next is not None:
        tmp = tmp.next
    # tmp == last
    sol.reorderList(n)
    #sol.revloop(n.next, 7)
    print(tmp2)

