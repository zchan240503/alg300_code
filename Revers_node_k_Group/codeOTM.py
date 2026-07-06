class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def reverseKGroup(self, head: ListNode, k: int) -> ListNode:
        prev = ListNode(0)
        cur = head
        
        while True:
            next_node = cur.next
            cur.next = prev
            prev = cur
            cur = next_node
            if cur.next is None:
                break
        return cur

def ListToArr(lists : ListNode | None):
        temp = lists
        arr = []
        while temp.next is not None:
            arr.append(temp.val)
            temp = temp.next
        arr.append(temp.val)
        return arr
def List2ListNode(lists):
    listnode = ListNode()
    tmp = listnode
    arr = []
    for l in lists:
        tmp.next = ListNode(l)
        tmp = tmp.next
        arr.append(tmp.val)
    print("check L2L :",arr)
    return listnode.next
a = Solution()
node = List2ListNode([1,2,3,4,5])
print("ket qua",ListToArr(a.reverseKGroup(node, 6)))
