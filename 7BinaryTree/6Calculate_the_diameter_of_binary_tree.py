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

    def max_diameter(self,root):
        if root is None:
            return 0
        result = [0]
        self.max_diameter_result(root, result)
        return result[0]

    def max_diameter_result(self, root, result):
        if root is None:
            return 0

        left=self.max_diameter_result(root.left,result)
        right=self.max_diameter_result(root.right,result)

        result[0] = max(result[0], left+right)

        return max(left,right)+1


binary = BinaryTree()

binary.root = binary.construct_tree()


result = binary.max_diameter(binary.root)
print("max diameter of binary tree is : ",result)