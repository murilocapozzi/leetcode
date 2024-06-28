class Solution(object):
    
    def maximumImportance(self, n: int, roads: list[list[int]]) -> int:
        
        # Passos para descobrir o grau de cada vértice
        graph = {}
        for road in roads:
            node1,node2 = road
            
            if node1 in graph: graph[node1] += 1
            else: graph[node1] = 1
            
            if node2 in graph: graph[node2] += 1
            else: graph[node2] = 1
        
        # Ordena-se pelo grau de forma decrescente
        graph = sorted(graph.items(), key=lambda item: item[1], reverse=True)
        
        # Passos para atribuir importância para as ruas
        # Quanto maior o grau, maior a importância das ruas dessa cidade
        importance = {}
        i = n
        for city in graph:
            importance[city[0]] = i
            i -= 1
        
        # Percorre novamente as ruas, somando as importâncias
        totalImportance = 0
        for road in roads:
            totalImportance += (importance[road[0]] + importance[road[1]])
        
        return totalImportance