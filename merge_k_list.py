class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def ListToArr(self, lists : ListNode | None):
        temp = lists
        arr = []
        while temp is not None:
            arr.append(temp.val)
            temp = temp.next
        return arr
    def List2ListNode(self, lists):
        listnode = ListNode()
        tmp = listnode
        for l in lists:
            tmp.val = l
            tmp = tmp.next
        return listnode
    def Merge_list(self, lists : ListNode | None):
        resuilt = []
        for l in lists:
            temp = l 
            while temp.next is not None:
                resuilt.append(temp.val)
                temp = temp.next
        resuilt.sort()
        return resuilt
def List2ListNode(lists):
        listnode = ListNode()
        tmp = listnode
        for i, l in enumerate(lists):
            tmp.val = l
            tmp.next = ListNode()
            tmp = tmp.next
        return listnode
a = Solution()
b = [[1,4,5],[1,3,4],[2,6]]
l = []
for lists in b:
    lists = List2ListNode(lists)
    l.append(lists)
print(a.Merge_list(l))