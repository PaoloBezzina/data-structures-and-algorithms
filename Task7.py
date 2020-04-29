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


def printTree(root, indent):
    
    space = 10

    if root is None:
        return

    indent = indent + space

    #process right side
    printTree(root.rightNode, indent)

    #process root
    for i in range(space, indent):
        print(end = " ")
    print(root.data)

    #process left side
    printTree(root.leftNode, indent)
    

#user input for integers
exit = bool(False)

root = Node(input("Input root node: "))

while exit is False:
    val = input("Input new value or -1 to exit: ")

    if val == -1:
        exit = bool(True)
    else:
        insertNode(root, Node(val))
        printTree(root, 0)