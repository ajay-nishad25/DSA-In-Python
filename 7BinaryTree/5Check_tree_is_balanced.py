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

    # approach 1
    def first_approach(self,root):
        if root is None:
            return True

        result = [0, True]
        self.generate_first_approach(root, result)
        return result[1]

    def generate_first_approach(self, root, result):
        if root is None:
            return [0, True]

        left_side = self.generate_first_approach(root.left, result)
        right_side = self.generate_first_approach(root.right, result)

        left_height = left_side[0]
        right_height = right_side[0]

        height = max(left_height,right_height)+1
        balance = abs(left_height-right_height)

        if balance > 1:
            result[1] = False

        return [height, result[1]]


    # approach 2
    def second_approach(self,root):
        if root is None:
            return True

        return self.generate_second_approach(root) != -1

    def generate_second_approach(self, root):
        if root == None:
            return 0

        left = self.generate_second_approach(root.left)
        if left == -1:
            return -1

        right = self.generate_second_approach(root.right)
        if right == -1:
            return -1

        if abs(left-right) > 1:
            return -1

        return max(left,right)+1


binary = BinaryTree()

binary.root = binary.construct_tree()


result = binary.first_approach(binary.root)
print("by 1st approach is tree is balanced : ",result)

result = binary.second_approach(binary.root)
print("by 2nd approach is tree is balanced : ",result)