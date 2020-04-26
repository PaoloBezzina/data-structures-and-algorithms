class Node:

    #__init__ is the class 'constructor
    #self is required to be able to access methods and attributes of the class 
    def __init__(self, value):
        self.leftNode = None
        self.rightNode = None
        self.data = value

#insert new node function
def insertNode(root, node):

    #check for root node
    if root is None:
        root = node
    else:
        if node.data < root.data:
            if root.leftNode is None:
                root.leftNode = node
            else:
                insertNode(root.leftNode, node)
        else:
            if root.rightNode is None:
                root.rightNode = node
            else:
                insertNode(root.rightNode, node)

def in_order_print(root):
    if not root:
        return
    in_order_print(root.leftNode)
    print root.data
    in_order_print(root.rightNode)


#user input for integers
exit = bool(False)

root = Node(input("Input root node: "))

while exit == False:
    val = input("Input new value or -1 to exit: ")

    if val == -1:
        exit = bool(True)
    else:
        insertNode(root, Node(val))

def printTree(root):
    