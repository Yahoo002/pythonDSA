class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeTwoLists(self, list1, list2):
        curr = dummy = ListNode()
        while list1 and list2:
            if list1.val < list2.val:
                curr.next = list1
                list1, curr = list1.next, list1
            else:
                curr.next = list2
                list2, curr = list2.next, list2

        if list1:
            curr.next = list1
        if list2:
            curr.next = list2
        return dummy.next


if __name__ == "__main__":
    merge = Solution()
    list1 = ListNode(2)
    list1.next = ListNode(3)
    list1.next.next = ListNode(4)

    list2 = ListNode(1)
    list2.next = ListNode(3)
    list2.next.next = ListNode(5)
    list2.next.next.next = ListNode(6)

    mergeList = merge.mergeTwoLists(list1, list2)

    while mergeList:
        print(mergeList.val, end=' -> ')
        mergeList = mergeList.next
    print('None')
