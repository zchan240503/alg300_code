class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def reverseKGroup(self, head: ListNode, k: int) -> ListNode:
        check_k = 0
        check_head = head
        while check_head:
            check_k += 1
            check_head =check_head.next
        if check_k < k:
            return None
        elif check_k ==0:
            return head
        temp = head
        resuitl = ListNode(0)
        res = resuitl
        save_next = ListNode(0)
        h = head
        count = 0
        arr = []
        check_arr = []
        k_group = ListNode(0)
        tmp_k = k_group
        while h :
            arr.append(h)
            save_next = h.next
            h.next = None
            h = save_next
            count +=1
            if count == k:
                for ln in arr:
                    tmp_k.next = ln
                    tmp_k = tmp_k.next
                    check_arr.append(tmp_k.val)
                res_swap = self.Swap_node(k_group.next)
                res.next = res_swap
                while res.next :
                    res = res.next
                arr = []
                count = 0
                k_group = ListNode(0)
                tmp_k = k_group
        for l in arr:
            res.next = l
            res = res.next
        return resuitl.next
    def Swap_node(self, head: ListNode)-> ListNode:
        stack = []
        resuilt = ListNode(0)
        temp = head
        save = resuilt
        while temp:
            stack.append(temp)
            temp = temp.next
        while stack:
            save.next = stack.pop()
            save = save.next
        save.next = None
        return resuilt.next
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
print("ket qua",ListToArr(a.reverseKGroup(node, 2)))
