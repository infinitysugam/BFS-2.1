# Time Complexity = O(n)
# Space Complexity = O(n)

from collections import deque

"""
# Definition for Employee.
class Employee:
    def __init__(self, id: int, importance: int, subordinates: List[int]):
        self.id = id
        self.importance = importance
        self.subordinates = subordinates
"""

class Solution:
    def getImportance(self, employees, id: int) -> int:

        hashmap = {}
        
        for i in employees:
            hashmap[i.id]=i

        queue = deque()

        for i in hashmap[id].subordinates:
            queue.append(i)
        
        importance = 0

        importance = importance + hashmap[id].importance

        while queue:
            element = queue.popleft()
            importance = importance+hashmap[element].importance
            for i in hashmap[element].subordinates:
                queue.append(i)
        
        return importance



