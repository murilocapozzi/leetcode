from collections import defaultdict


class Solution:
    
    def dfs(self, graph, ancestor, current, ans, visited):
        
        # Lista de vértices já visitados, para evitar ciclos e redundâncias
        visited[current] = 1
        
        for adj in graph[current]:
            
            # Se o adjacente ainda não foi explorado, aplica DFS nele também
            # E insere na resposta o parentesco
            if not visited[adj]:
                ans[adj].append(ancestor)
                self.dfs(graph, ancestor, adj, ans, visited)
            
    
    def getAncestors(self, n: int, edges: list[list[int]]) -> list[list[int]]:

        graph = {i: [] for i in range(n)}
        ans = [[] for _ in range(n)]

        # Preenche o grafo na forma de lista de adjacência
        for edge in edges:
            graph[edge[0]].append(edge[1])
            
        # Aplica a busca em profundidade em cada vértice
        for i in range(n):
            self.dfs(graph, i, i, ans, [0] * n)
        
        # Ao final, ordena o parentesco de cada vértice
        for i in range(n):
            ans[i].sort()
            
        return ans