
class Node:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None


class BinaryTree:
    def __init__(self):
        self.root = None

    def is_empty(self):
        return self.root == None

    def construct_tree(self):

        data = int(input("Enter node data : "))
        # -1 means no node
        if data == -1:
            return None

        new_node = Node(data)

        # since now we have data for the root node lets move to left node of root

        print("Enter left node data : ")
        new_node.left = self.construct_tree()

        print("Enter right node data : ")
        new_node.right = self.construct_tree()

        return new_node

    def inorder_traversal(self,root):
        if root == None:
            return
        self.inorder_traversal(root.left)
        print(root.data, end =" ")
        self.inorder_traversal(root.right)

    def preorder_traversal(self,root):
        if root == None:
            return
        print(root.data, end=" ")
        self.preorder_traversal(root.left)
        self.preorder_traversal(root.right)

    def postorder_traversal(self,root):
        if root == None:
            return
        self.postorder_traversal(root.left)
        self.postorder_traversal(root.right)
        print(root.data, end=" ")



binary = BinaryTree()

binary.root = binary.construct_tree()
root_node = binary.root

print("Inorder Traversal : ")
binary.inorder_traversal(root_node)

print()
print("Preorder Traversal : ")
binary.preorder_traversal(root_node)

print()
print("Postorder Traversal : ")
binary.postorder_traversal(root_node)

