class Node:
    def __init__(self,data):
        self.data=data
        self.children=[]
        self.parent=None
    def add(self,child):
        self.children.append(child)

def buildTree():
    head=Node("1")
    n1=Node("2")
    n2=Node("3")
    head.add(n1)
    head.add(n2)








if __name__ =='__main__':
    buildTree()