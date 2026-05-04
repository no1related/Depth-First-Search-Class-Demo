from trees import tree1, tree2, tree3
from preorder import preorder
from inorder import inorder
from postorder import postorder

print("TREE 1")
print("Preorder: ", end="")
preorder(tree1)
print("\nInorder: ", end="")
inorder(tree1)
print("\nPostorder:", end=" ")
postorder(tree1)

print("\n\nTREE 2")
print("Preorder: ", end="")
preorder(tree2)
print("\nInorder: ", end="")
inorder(tree2)
print("\nPostorder:", end=" ")
postorder(tree2)

print("\n\nTREE 3")
print("Preorder: ", end="")
preorder(tree3)
print("\nInorder: ", end="")
inorder(tree3)
print("\nPostorder:", end=" ")
postorder(tree3)
