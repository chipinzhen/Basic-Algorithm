from BTreeNode import BST, BTreeNode

a = [52, 31, 17, 81, 22, 35, 29, 71, 44, 55, 66, 10, 2, 5, 1, 3]
bst = BST(a)

bst.inOrderTraverse(bst.root)
print (bst.root.value)

bst.delete(bst.root, 52)
print(bst.root.value)
bst.inOrderTraverse(bst.root)