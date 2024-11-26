class node:
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None
    def add(self,data):
        if data ==self.data:
            return
        elif data<self.data:
            if self.left:
                self.left.add(data)
            else:
               self.left=node(data)
        elif data>self.data:
            if self.right:
                self.right.add(data)
            else:
               self.right=node(data)
    def search(self,val):
        if val ==self.data:
            return True
        elif val<self.data:
            if self.left:
                return self.left.search(val)
        elif val>self.data:
            if self.right:
                return self.right.search(val)
        return False
    def min(self):
        if not self.left:
            return self.data
        else:
            return self.left.min()
    def max(self):
        if not self.right:
            return self.data
        else:
            return self.right.max()    
    def delete(self,val):
        if self.search(val):
            if val<self.data:
                self.left=self.left.delete(val)
            elif val>self.data:
                self.right=self.right.delete(val)
            else:
                if self.left is None and self.right is None:
                    return None
                elif self.left is None:
                    return self.right
                elif self.right is None:
                    return self.left 
                max=self.left.max()
                self.data= max
                self.left=self.left.delete(max)
        return self
    def iot(self):
        elements=[]
        if(self.left):
            elements+=self.left.iot()
        elements.append(self.data)
        if (self.right):
            elements+=self.right.iot()
        return elements

def buildTree(elements):
    root = node(elements[0])
    for i in range(1,len(elements)):
        root.add(elements[i])
    return root

if __name__ == "__main__":
    root =buildTree([5,1,74,8,99,10])
    print(root.iot())
    root.delete(5)
    print(root.iot())
    
