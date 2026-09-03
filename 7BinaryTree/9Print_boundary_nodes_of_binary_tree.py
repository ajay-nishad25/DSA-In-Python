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
    
    def boundary_traversal(self, root):
        result = [root.data]
        if root.left is None and root.right is None:
            return [root.data]
        self.left_side(root.left, result)
        self.leaf_nodes(root, result)
        self.right_side(root.right, result)
        return result
        
    def left_side(self, root, result):
        if root is None:
            return
        if root.left is None and root.right is None:
            return 
        result.append(root.data)
        if root.left:
            self.left_side(root.left, result)
        else:
            self.left_side(root.right, result)
    
    def right_side(self, root, result):
        if root is None:
            return
        if root.left is None and root.right is None:
            return
        if root.right:
            self.right_side(root.right, result)
        else:
            self.right_side(root.left, result)
        result.append(root.data)
    
    def leaf_nodes(self, root, result):
        if root is None :
            return
        if root.left is None and root.right is None:
            result.append(root.data)
            return
        self.leaf_nodes(root.left, result)
        self.leaf_nodes(root.right, result)


binary = BinaryTree()

binary.root = binary.construct_tree()

print("Boundary values of binary tree : ", binary.boundary_traversal(binary.root))