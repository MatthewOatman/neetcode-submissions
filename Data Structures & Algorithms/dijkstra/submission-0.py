import heapq
class Solution:
    def shortestPath(self, n: int, edges: List[List[int]], src: int) -> Dict[int, int]:

        '''
        Dijksta's is done with a min_heap
        the shortest current path is at the beginning of the heap

        return the shortest distance from every vertex in the graph

        The priority queue always selects the node with the smallest current       distance, ensuring that we explore the shortest paths first and avoid unnecessary processing of longer paths

        Dijkstra's is a greedy bfs

        '''

        # Step #1 convert the edges into an adjaceny list
        adj = {}
        for i in range(n):
            adj[i] = []

        # adjaceny list = {src : [[dest1, weight], [dest2, weight], ...]}
        for s, d, weight in edges:
            adj[s].append([d, weight])

        shortest = {} # Map a vertex -> dist of shortest path

        # Step 2: Initialize the minHeap with src node and 0 distance from it
        minHeap = [(0, src)]
        while minHeap:
            w1, n1 = heapq.heappop(minHeap)
            if n1 in shortest:
                continue

            shortest[n1] = w1

            for n2, w2 in adj[n1]:
                if n2 not in shortest:
                    heapq.heappush(minHeap, [w2 + w1, n2])

        for i in range(n):
            if i not in shortest:
                shortest[i] = -1

        return shortest

        

