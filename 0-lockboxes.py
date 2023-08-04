#!usr/bin/python3
import typing import List

def canUnlockAll(boxes: List[List[int]]) -> bool:
    n = len(boxes)
    visited = [False] * n
    visited[0] = True
    queue = [0]
                        
    while queue:
        box = queue.pop(0)
        for key in boxes[box]:
            if not visited[key]:
                visited[key] = True
                queue.append(key)
    return all(visited)
