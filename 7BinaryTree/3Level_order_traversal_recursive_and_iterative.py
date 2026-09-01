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


    def levelorder_iterative(self,root):
        if root == None:
            return []
        queue =  deque([root])
        result = []
        
        while queue:
            size = len(queue)
            inner_result = []
            for i in range(size):
                node = queue.popleft()
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
                
                if node :
                    inner_result.append(node.data)
            
            result.append(inner_result)
        
        return result

    def generate_recursive_result(self,root, result, level):
        if root is None:
            return
        
        if len(result) <= level:
            result.append([])
        
        result[level].append(root.data)
        self.generate_recursive_result(root.left, result, level+1)
        self.generate_recursive_result(root.right, result, level+1)

    def levelorder_recursive(self, root):
        if root is None:
            return []
        result = []
        self.generate_recursive_result(root, result, 0)
        return result





binary = BinaryTree()

binary.root = binary.construct_tree()


levelorder_result = binary.levelorder_iterative(binary.root)
print("Result of level order itertative : ",levelorder_result)


levelorder_recursive_result = binary.levelorder_recursive(binary.root)
print("Result of level order recursive : ",levelorder_recursive_result)
