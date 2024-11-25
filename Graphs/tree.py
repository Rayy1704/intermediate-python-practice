class Node:
    def __init__(self,data):
        self.data=data
        self.children=[]
        self.parent=None
    def add(self,child):
        child.parent=self
        self.children.append(child)

    def display(self):
        print(f"{"\t"*self.getLevel()}{self.data}")
        for child in self.children:
            child.display()

def buildTree():
    root=Node("Electronics")
    e1=Node("Laptops")
    e1.add(Node("Macbooks"))
    e1.add(Node("ThinkPads"))
    e1.add(Node("EliteBooks"))
    e2=Node("Mobile Phones")
    e2.add(Node("iPhone"))
    e2.add(Node("Galaxy"))
    e2.add(Node("Pixel"))
    e3=Node("Desktops")
    e3.add(Node("AlienWare"))
    e3.add(Node("Omen"))
    e3.add(Node("Custom"))
    root.add(e1)
    root.add(e2)
    root.add(e3)
    return root









if __name__ =='__main__':
    root=buildTree()
    root.display()