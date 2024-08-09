# Definition for a binary tree node.
from typing import Optional


class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
        
class Solution(object):
    def arrToTree(self, arr, i=0):
        
        if i >= len(arr) or arr[i] == None: return None
        
        left = self.arrToTree(arr, 2*i+1)
        right = self.arrToTree(arr, 2*i+2)
        
        return TreeNode(val=arr[i], left=left, right=right)
    
    def treeToArr(self, root, arr, i):
        
        if not root: 
            arr.insert(i, None)
            return
        
        arr.insert(i, root.val)
        if root.left or root.right:
            self.treeToArr(root.left, arr, (2*i) + 1)
            self.treeToArr(root.right, arr, (2*i) + 2)
        
    def createBinaryTree(self, descriptions: list[list[int]]) -> Optional[TreeNode]:

        # Dicionário que irá indexar pelo valor do nó (que é único)
        # junto com ele os seus filhos e o seu pai
        nodes = {}

        # Extrai da descrição as informações e atualiza ou cria os campos do nó
        for description in descriptions:
            parent = description[0]
            child = description[1]
            isLeft = description[2]

            if parent in nodes:
                # Atualiza
                if isLeft: nodes[parent]['left'] = child
                else: nodes[parent]['right'] = child
            else:
                # Cria
                if isLeft: nodes[parent] = {'left': child, 'right': None, 'parent': None}
                else: nodes[parent] = {'left': None, 'right': child, 'parent': None}

            # Cria ou atualiza no filho criado a referência do pai
            if child in nodes: nodes[child]['parent'] = parent
            else: nodes[child] = {'left': None, 'right': None, 'parent': parent}

        node = list(nodes.keys())[0]

        # Procura pelo único nó que não possui pai, ou seja, a raiz
        while nodes[node]['parent'] != None:
            node = nodes[node]['parent']

        def buildTree(root, nodes) -> Optional[TreeNode]:
        # Desce de forma prefixa, criando das folhas até a raiz

            if not root: return None

            left = buildTree(nodes[root]['left'], nodes)
            right = buildTree(nodes[root]['right'], nodes)

            return TreeNode(val=root, left=left, right=right)

        # Com a raiz e a informação de todos guardada, cria a árvore
        return buildTree(node, nodes)
