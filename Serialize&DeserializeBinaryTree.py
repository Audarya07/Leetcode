# Input: root = [1,2,3,null,null,4,5]
# Output: [1,2,3,null,null,4,5]

class Codec:
    
    def serialize(self, root):
        #node(left_subtree),(right_subtree)
        #1(2(X),(X)),(3(4(X),(X)),(5(X),(X)))
        if not root:
            return "X"
        return str(root.val)+"("+self.serialize(root.left)+"),("+self.serialize(root.right)+")"
        
    def deserialize(self, data):    #data = 1(2(X),(X)),(3(4(X),(X)),(5(X),(X)))
        if data == "X":
            return None
        #1  --> data[0]
        #2(X),(X)),(3(4(X),(X)),(5(X),(X)))   --> data[1]
        
        data = data.split("(", 1)   #split on ( only for 1 time i.e 1st occurence
        node = TreeNode(data[0])    #node 1
        data = "("+data[1]          #(2(X),(X)),(3(4(X),(X)),(5(X),(X)))
        i = 0
        cnt = 0
        for i in range(len(data)):
            ch = data[i]
            if ch == "(":
                cnt += 1
            elif ch == ")":
                cnt -= 1
                if cnt == 0:    #(2(X),(X))
                    node.left = self.deserialize(data[1:i])     #2(X),(X)
                    node.right = self.deserialize(data[i+3:-1]) #3(4(X),(X)),(5(X),(X)
                    return node
        
# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))