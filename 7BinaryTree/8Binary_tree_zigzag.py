from collections import deque



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

    def zigzag(self,root):
        if root is None:
            return []
        result = []
        self.generate_zigzag(root, result)
        return result

    def generate_zigzag(self, root, result):
        queue = deque([root])
        toggle = False

        while queue:
            n = len(queue)
            inner_result = []

            for i in range(n):
                node = queue.popleft()
                if node:
                    inner_result.append(node.data)
                    if node.left :
                        queue.append(node.left)
                    if node.right:
                        queue.append(node.right)

            if toggle:
                inner_result.reverse()
            result.append(inner_result)
            toggle = not toggle


binary = BinaryTree()

binary.root = binary.construct_tree()

print("ZigZag result of binary tree : ", binary.zigzag(binary.root))