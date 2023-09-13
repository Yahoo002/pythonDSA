class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:

    def __init__(self):
        self.head = None

    def insertAtBeginning(self, new_data):
        new_node = Node(new_data)

        new_node.next = self.head
        self.head = new_node

    def insertAfter(self, prev_node, new_data):
        if prev_node is None:
            print("The given previous node must be in LinkedList")
            return

        new_node = Node(new_data)
        new_node.next = prev_node.next
        prev_node.next = new_node

    def insertAtEnd(self, new_data):
        new_node = Node(new_data)

        if self.head is None:
            self.head = new_node
            return

        last = self.head
        while (last.next):
            last = last.next

        last.next = new_node

    def deleteNode(self, position):
        if self.head is None:
            return

        temp = self.head

        if temp is None:
            return

        if temp.next is None:
            return

        if position == 1:
            self.head = temp.next
            temp = None
            return

        for i in range(position - 1):
            temp = temp.next
            if temp is None:
                break

        next = temp.next.next
        temp.next = None
        temp.next = next

    def search(self, key):
        current = self.head

        while current is not None:
            if current.data == key:
                return True

            current = current.next

        return False

    # merge sort

    def merge_sort(self, head):
        if head is None or head.next is None:
            return head

        middle = self.get_middle(head)
        left_half = head
        right_half = middle.next
        middle.next = None

        left_sorted = self.merge_sort(left_half)
        right_sorted = self.merge_sort(right_half)

        sorted_list = self.merge(left_sorted, right_sorted)

        return sorted_list

    def get_middle(self, head):
        slow = head
        fast = head

        while fast.next is not None and fast.next.next is not None:
            slow = slow.next
            fast = fast.next.next

        return slow

    def merge(self, left, right):
        dummy = Node(0)
        current = dummy

        while left is not None and right is not None:
            if left.data < right.data:
                current.next = left
                left = left.next
            else:
                current.next = right
                right = right.next
            current = current.next

        if left is not None:
            current.next = left
        elif right is not None:
            current.next = right

        return dummy.next

    def printList(self):
        temp = self.head
        while (temp):
            print(str(temp.data) + '', end="  ")
            temp = temp.next


if __name__ == '__main__':
    llist = LinkedList()
    llist.insertAtEnd(1)
    llist.insertAtBeginning(2)
    llist.insertAtBeginning(3)
    llist.insertAtEnd(4)
    llist.insertAfter(llist.head.next, 5)

    print('Linked list:')
    llist.printList()

    print("\nAfter deleting an element: ")
    llist.deleteNode(3)
    llist.printList()

    print()
    item_to_find = 3
    if llist.search(item_to_find):
        print(str(item_to_find) + " is found")
    else:
        print(str(item_to_find) + " is not found")

    llist.head = llist.merge_sort(llist.head)
    print("Sorted List: ")
    llist.printList()
