from typing import List

class ListNode:
    def __init__(self, number: int = 0):
        self.number: int = number
        self.connections: List[int] = []

class Solution:
    def possibleBipartition(self, N: int, dislikes: List[List[int]]) -> bool:
        DISLIKER: int = 0
        DISLIKED: int = 1
        nodes: List[ListNode] = []
        
        for n in range(N):
            nodes.append(ListNode(n))
        
        for dislike in dislikes:
            left = dislike[DISLIKER] - 1
            right = dislike[DISLIKED] - 1
            nodes[left].connections.append(right)

        for node in nodes:
            connections = [] + node.connections
            while connections:

                connection = connections.pop(0)
                connections = nodes[connection].connections + connections

                if connection in connections:
                    return False
        return True
                    

class Main:
    def exec(self):
        listnode = ListNode()
        solution = Solution()
        for test in self.test():
            print(solution.possibleBipartition(test[0], test[1]))

    def test(self):
        return [
                [4, [[1,2],[1,3],[2,4]]],
                [3, [[1,2],[1,3],[2,3]]],
                [5, [[1,2],[2,3],[3,4],[4,5],[1,5]]],
                [10, [[4,7],[4,8],[5,6],[1,6],[3,7],[2,5],[5,8],[1,2],[4,9],[6,10],[8,10],[3,6],[2,10],[9,10],[3,9],[2,3],[1,9],[4,6],[5,7],[3,8],[1,8],[1,7],[2,4]]]
               ]

main = Main()
main.exec()