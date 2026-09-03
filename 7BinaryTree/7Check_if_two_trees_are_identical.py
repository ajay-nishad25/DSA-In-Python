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

    def print_tree(self,root):
        if root is None:
            return
        self.print_tree(root.left)
        print(root.data, end =" ")
        self.print_tree(root.right)

    def is_tree_identical(self,root1, root2):
        if root1 is None and root2 is None:
            return True

        # if any of them becomes none then return False
        if root1 is None or root2 is None:
            return False

        # if there data is not same
        if root1.data != root2.data:
            return False

        return self.is_tree_identical(root1.left, root2.left) and self.is_tree_identical(root1.right, root2.right)


print("Create 1st Tree")


binary1 = BinaryTree()
binary1.root = binary1.construct_tree()
binary1.print_tree(binary1.root)

print()
print("Create 2nd Tree")

binary2 = BinaryTree()
binary2.root = binary2.construct_tree()
binary2.print_tree(binary2.root)

print()
result = binary1.is_tree_identical(binary1.root,binary2.root)
print("is both tree identical : ",result)
