class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def ListToArr(self, list : ListNode | None):
        temp = list
        arr = []
        while temp is not None:
            arr.append(temp.val)
            temp = temp.next
        return arr

    def mergeTwoLists(self, list1: ListNode | None, list2: ListNode | None) -> ListNode | None:
        temp_list1 = self.ListToArr(list1)
        temp_list2 = self.ListToArr(list2)
        temp_list1.sort()
        temp_list2.sort()
        i , j = 0, 0
        merge_list = []
        while j < len(temp_list2) and i < len(temp_list1):
            if temp_list1[i] <= temp_list2[j]:
                merge_list.append(temp_list1[i])
                i+=1
            else :
                merge_list.append(temp_list2[j])
                j+=1
        index = 0
        new_ListNode = ListNode(0)
        for value in merge_list:
            new_ListNode.next = ListNode(value)
            new_ListNode = new_ListNode.next
        return new_ListNode.next
a = Solution()
print(a.mergeTwoLists(list1=[1,2,4], list2=[1,3,4]))