class Solution(object):
    def findCenter(self, edges):
        # Basta achar qual elemento repete nas duas primeiras arestas dadas, o repetido é o centro
        if edges[0][0] == edges[1][1] or edges[0][0] == edges[1][0]:
            return edges[0][0]
        return edges[0][1]