class BTreeNode:
    def __init__(self, value):
        self.value = value
        self.lchild = None
        self.rchild = None
        self.parent = None

class BST:

    def __init__(self, node_list):
        self.root = BTreeNode(node_list[0])
        for value in node_list[1:]:
            self.insert(self.root, None, value)


    def create_root(self, node):
        if node.parent == None:
            print("This node can be used as root")

    #使用search方法时， 函数的node输入必须为根节点。
    def search(self, node, parent, value):
        if node is None:
            return False
        if node.value == value:
            return node, parent
        elif value < node.value:
            self.search(node.lchild, node, value)
        elif value > node.value:
            self.search(node.rchild, node, value)

    #使用insert方法时, 函数的node输入必须为根节点。
    def insert(self, node, parent, value):
        if node is None:
            new_node = BTreeNode(value)
            new_node.parent = parent
            if value < parent.value:
                parent.lchild = new_node
            elif value > parent.value:
                parent.rchild = new_node
            return
        if node.value == value:
            print("It's none of necessity to insert value, because of repeated value.")
        elif node.value > value:
            self.insert(node.lchild, node, value)
        elif node.value < value:
            self.insert(node.rchild, node, value)

    def delete(self, rootnode, value):
        checknode, nodeparent = self.search(rootnode, None, value)
        if checknode is False:
            print("Can't delete, the aim node doesn't exist.")
        else:
            if (checknode.lchild is None) & (checknode.rchild is None):
                checknode = None

            elif (checknode.lchild is None) & (checknode.rchild is not None):
                if nodeparent.value < checknode.rchild.value:
                    nodeparent.rchild = checknode.rchild
                else:
                    nodeparent.lchild = checknode.rchild

            elif (checknode.lchild is not None) & (checknode.rchild is None):
                if nodeparent.value < checknode.lchild.value:
                    nodeparent.rchild = checknode.lchild
                else:
                    nodeparent.lchild = checknode.lchild

            elif (checknode.lchild is not None) & (checknode.rchild is not None):
                nodetemp = checknode.rchild
                while nodetemp.lchild is not None:
                    nodetemp = nodetemp.lchild
                new_node = BTreeNode(nodetemp.value)
                new_node.lchild = checknode.lchild
                new_node.rchild = checknode.rchild

                if nodeparent is not None:
                    if new_node.value < nodeparent.value:
                        nodeparent.lchild = new_node
                    else:
                        nodeparent.rchild = new_node
                else:
                    self.root = new_node
                checknode = None
                nodetemp = None

                # 先序遍历
    def preOrderTraverse(self, node):
        if node is not None:
            print (node.value)
            self.preOrderTraverse(node.lchild)
            self.preOrderTraverse(node.rchild)

    # 中序遍历
    def inOrderTraverse(self, node):
        if node is not None:
            self.inOrderTraverse(node.lchild)
            print (node.value)
            self.inOrderTraverse(node.rchild)

    # 后序遍历
    def postOrderTraverse(self, node):
        if node is not None:
            self.postOrderTraverse(node.lchild)
            self.postOrderTraverse(node.rchild)
            print (node.value)