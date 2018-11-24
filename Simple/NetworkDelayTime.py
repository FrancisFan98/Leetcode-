class Solution(object):
    def networkDelayTime(self, times, N, K):
        """
        :type times: List[List[int]]
        :type N: int
        :type K: int
        :rtype: int
        """
        pathes = collections.defaultdict(list)
        for u, w, v in times:
            pathes[u].append((v,w))
            
        time = {i:float("inf") for i in range(1, N+1)}
        
        def dfs(node, elapsed):
            if elapsed >= time[node]:
                return
            time[node] = elapsed
            for cost, nex in sorted(pathes[node]):
                dfs(nex, cost+elapsed)
        
        dfs(K, 0)
        
        return max(time.values()) if max(time.values()) != float("inf") else -1
        `
