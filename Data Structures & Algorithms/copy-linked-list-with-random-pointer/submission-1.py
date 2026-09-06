"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        hash_map = {}

        if not head:
            return None
        
        temp = head
        new_head = None
        while temp:
            if not new_head:
                new_head = Node(temp.val, None, temp.random)
                new_temp = new_head
                hash_map[temp] = new_head
            else:
                new_temp.next = Node(temp.val,None, temp.random)
                hash_map[temp] = new_temp.next
                new_temp = new_temp.next
            temp = temp.next
        hash_map[None] = None

        for key, val in hash_map.items():
            if key == None or val == None:
                print(None, None)
                continue
            print(key.val, val.val)
        new_temp = new_head
        while new_temp:
            new_temp.random = hash_map[new_temp.random]
            new_temp = new_temp.next


        new_temp = new_head
        temp = head
        while new_temp:
            print(new_temp.val)
            new_temp = new_temp.next
        
        while temp:
            print(temp.val)
            temp = temp.next
        

        temp = head
        new_temp = new_head



        return new_head