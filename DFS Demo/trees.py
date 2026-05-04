from node import Node

# =========================
# Tree 1: Simple Tree
# =========================
tree1 = Node('A')
tree1.left = Node('B')
tree1.right = Node('C')
tree1.left.left = Node('D')
tree1.left.right = Node('E')
tree1.right.right = Node('F')


# =========================
# Tree 2: Larger Structured Tree
# =========================
tree2 = Node('H')
tree2.left = Node('D')
tree2.right = Node('L')

tree2.left.left = Node('B')
tree2.left.right = Node('F')

tree2.left.left.left = Node('A')
tree2.left.left.right = Node('C')

tree2.right.left = Node('J')
tree2.right.right = Node('N')
tree2.right.left.right = Node('K')


# =========================
# Tree 3: Jumbled / Irregular Tree
# =========================
tree3 = Node('M')
tree3.left = Node('T')
tree3.right = Node('E')

tree3.left.right = Node('A')
tree3.left.right.left = Node('Z')

tree3.right.left = Node('R')
tree3.right.left.right = Node('B')