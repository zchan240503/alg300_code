class ListNode:
    def __init__(self, val=0, next = None):
        self.val = val
        self.next = next
class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        new_list = ListNode()
        new_list_run = new_list
        node_right = ListNode()
        node_left = ListNode()
        temp_node = head
        arr = []
        while temp_node is not None and temp_node.next is not None:
            
            node_right = temp_node
            node_left = temp_node.next           
            temp = temp_node.next.next

            new_list_run.next = node_left
            arr.append(node_left.val)
            new_list_run = new_list_run.next
            new_list_run.next = node_right
            arr.append(node_right.val)
            new_list_run = new_list_run.next
            new_list_run.next = None
            temp_node = temp
        print("check : ",arr)
        return new_list
    def List2ListNode(self, lists):
        listnode = ListNode()
        tmp = listnode
        arr = []
        for l in lists:
            tmp.next = ListNode(l)
            tmp = tmp.next
            arr.append(tmp.val)
        print("check L2L :",arr)
        return listnode.next
def ListToArr(lists : ListNode | None):
        temp = lists
        arr = []
        while temp.next is not None:
            arr.append(temp.val)
            temp = temp.next
        arr.append(temp.val)
        return arr
a = Solution()
input = [1,2,3,4]
Node = a.List2ListNode(input)
print("check L2A :",ListToArr(Node))
print(ListToArr(a.swapPairs(Node)))