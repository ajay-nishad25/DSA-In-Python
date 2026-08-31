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


    def preorder_iterative(self,root):
        result = []
        stack = [root]

        while stack:
            node = stack.pop()
            if node:
                result.append(node.data)
                stack.append(node.right)
                stack.append(node.left)

        return result

    def inorder_iterative(self,root):
        result = []
        stack = []
        node = root
        while True:
            if node != None:
                stack.append(node)
                node = node.left
            else:
                if not stack:
                    break
                node = stack.pop()
                result.append(node.data)
                node = node.right

        return result



binary = BinaryTree()

binary.root = binary.construct_tree()


preorder_result = binary.preorder_iterative(binary.root)
print("Result of preorder itertative : ",preorder_result)


inorder_result = binary.inorder_iterative(binary.root)
print("Result of inorder itertative : ",inorder_result)
