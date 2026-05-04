from node import Node

#  LEFT  A      RIGHT
#       / \
#      B   C
#     / \   \
#    D   E   F
# Tree 1: Simple Tree
tree1 = Node('A')
tree1.left = Node('B')
tree1.right = Node('C')
tree1.left.left = Node('D')
tree1.left.right = Node('E')
tree1.right.right = Node('F')


# LEFT           F          RIGHT
#              /   \
#             D     I
#            / \   / \
#           B   E G   J
#          / \     \
#         A   C     H
# Tree 2: Large Tree
tree2 = Node('F')
tree2.left = Node('D')
tree2.right = Node('I')

tree2.left.left = Node('B')
tree2.left.right = Node('E')

tree2.left.left.left = Node('A')
tree2.left.left.right = Node('C')

tree2.right.left = Node('G')
tree2.right.right = Node('J')
tree2.right.left.right = Node('H')

#   LEFT         M      RIGHT
#              /   \
#             T     E
#              \   /
#               A R
#              /   \
#             Z     B
# Tree 3: Mixed Tree 
tree3 = Node('M')
tree3.left = Node('T')
tree3.right = Node('E')

tree3.left.right = Node('A')
tree3.left.right.left = Node('Z')

tree3.right.left = Node('R')
tree3.right.left.right = Node('B')