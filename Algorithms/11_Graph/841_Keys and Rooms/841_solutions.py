class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        queue=[]+rooms[0]
        n=len(rooms)
        visited=[False for _ in range(n)]
        visited[0]=True
        while queue:
            cur=queue.pop(0)
            visited[cur]=True
            for key in rooms[cur]:
                if not visited[key]:
                    queue.append(key)
                
        if False in visited:
            return False
        else:
            return True