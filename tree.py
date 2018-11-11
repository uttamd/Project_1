class Node:
    def __init__(self, value = None):
        self.data = value
        self.left_child = None
        self.right_child = None

    def insert(root, value):
        new = Node(value)
        if root == None:
            root = new
        else :
            while True:
                if root < new.value:
                    #go right
                    

