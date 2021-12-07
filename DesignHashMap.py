class Node:
    def __init__(self, key, val):
        self.pair = (key, val)
        self.next = None

class MyHashMap:

    def __init__(self):
        self.size = 1000
        self.my_map = [None for i in range(self.size)]

    def put(self, key: int, value: int) -> None:
        my_hash = key % self.size
        if self.my_map[my_hash] == None:
            self.my_map[my_hash] = Node(key, value)
        else:
            curr = self.my_map[my_hash]
            while True:
                if curr.pair[0] == key:
                    curr.pair = (key, value)
                    return
                
                if curr.next == None:
                    break
                curr = curr.next
            curr.next = Node(key, value)
        
    def get(self, key: int) -> int:
        my_hash = key % self.size
        curr = self.my_map[my_hash]
        
        while curr:
            if curr.pair[0] == key:
                return curr.pair[1]
            else:
                curr = curr.next
        return -1

    def remove(self, key: int) -> None:
        my_hash = key % self.size
        curr = self.my_map[my_hash]
        prev = self.my_map[my_hash]
        
        if not curr:
            return
        if curr.pair[0] == key:
            self.my_map[my_hash] = curr.next
            
        else:
            curr = curr.next
            while curr:
                if curr.pair[0] == key:
                    prev.next = curr.next
                    break
                else:
                    curr = curr.next
                    prev = prev.next
                    
                    
# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)