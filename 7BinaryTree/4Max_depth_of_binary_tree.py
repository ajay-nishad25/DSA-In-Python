class Node:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None


class BinaryTree:
    def __init__(self):
        self.root = None

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

    def max_depth(self,root):
        if root == None:
            return 0

        left = self.max_depth(root.left) + 1
        right = self.max_depth(root.right) + 1

        return max(left,right)

binary = BinaryTree()

binary.root = binary.construct_tree()


result = binary.max_depth(binary.root)
print("Max depth of binary tree is : ",result)
