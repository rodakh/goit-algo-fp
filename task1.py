class ListNode:
    def __init__(self, value=0, next=None):
        self.value = value
        self.next = next


def reverse_list(head):
    prev = None
    current = head
    while current is not None:
        next_node = current.next
        current.next = prev
        prev = current
        current = next_node
    return prev


def insertion_sort_list(head):
    dummy = ListNode(0)
    current = head
    while current is not None:
        prev = dummy
        next_node = current.next
        while prev.next is not None and prev.next.value < current.value:
            prev = prev.next
        current.next = prev.next
        prev.next = current
        current = next_node
    return dummy.next


def merge_two_sorted_lists(l1, l2):
    dummy = ListNode(0)
    tail = dummy
    while l1 is not None and l2 is not None:
        if l1.value < l2.value:
            tail.next = l1
            l1 = l1.next
        else:
            tail.next = l2
            l2 = l2.next
        tail = tail.next
    if l1 is not None:
        tail.next = l1
    else:
        tail.next = l2
    return dummy.next


def print_list(node):
    while node:
        print(node.value, end=" -> ")
        node = node.next
    print("None")


if __name__ == "__main__":
    list1 = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))
    print("Original list:")
    print_list(list1)
    list1 = reverse_list(list1)
    print("Reversed list:")
    print_list(list1)

    list2 = ListNode(4, ListNode(2, ListNode(1, ListNode(3))))
    print("Unsorted list:")
    print_list(list2)
    list2 = insertion_sort_list(list2)
    print("Sorted list:")
    print_list(list2)

    list3 = ListNode(1, ListNode(2, ListNode(4)))
    list4 = ListNode(1, ListNode(3, ListNode(4)))
    print("List 1:")
    print_list(list3)
    print("List 2:")
    print_list(list4)
    merged_list = merge_two_sorted_lists(list3, list4)
    print("Merged sorted list:")
    print_list(merged_list)
