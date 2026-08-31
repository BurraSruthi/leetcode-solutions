# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def nodesBetweenCriticalPoints(self, head: Optional[ListNode]) -> List[int]:
        first = -1
        last = -1
        
        min_dist = float('inf')
        max_dist = 0
        
        pos = 1
        
        prev = head
        curr = head.next
        
        while curr.next:
            # Check if curr is a critical point
            if ((curr.val > prev.val and curr.val > curr.next.val) or
                (curr.val < prev.val and curr.val < curr.next.val)):
                
                # First critical point
                if first == -1:
                    first = pos
                
                # We already have a previous critical point
                else:
                    min_dist = min(min_dist, pos - last)
                    max_dist = pos - first
                
                last = pos
            
            prev = curr
            curr = curr.next
            pos += 1
        
        if first == last:
            return [-1, -1]
        
        return [min_dist, max_dist]