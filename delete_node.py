# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
def cout_Node(head : ListNode):
    temp = head
    count = 0
    while temp.next != None:
        count+=1
        temp = temp.next
    if temp == None:
        return 0
    else:
        count+=1
        return count

class Solution:
    def removeNthFromEnd(self,head : ListNode, n):
        index = -cout_Node(head)
        temp = ListNode()
        h = head
        if cout_Node(head) == 1 :
            return []
        elif n == 1:
            while index < -n-1:
                h = h.next
                index+=1
            h.next = None
        elif n == cout_Node(head):
            head = head.next
            return head
        else:
            while index < -n-1:
                h = h.next
                index+=1
            temp = h.next.next
            h.next = None
            h.next = temp
        return head
def create_linked_list(arr):
    if not arr:
        return None
    head = ListNode(arr[0])
    current = head
    for value in arr[1:]:
        current.next = ListNode(value)
        current = current.next
    return head
def print_list(node):
    result = []
    current = node
    while current:
        result.append(str(current.val))  # Nhặt giá trị của Node
        current = current.next           # Nhảy sang Node tiếp theo
    print(" -> ".join(result))
head = create_linked_list([1])    
a = Solution()
res = a.removeNthFromEnd(head=head, n = 1)
print_list(res)

