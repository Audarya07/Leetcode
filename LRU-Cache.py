class Node:
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.prev = None
        self.next = None

class LRUCache:
    def __init__(self, capacity: int):
        self.cap = capacity
        self.mp = {}
        self.head = Node(0, 0)
        self.tail = Node(0, 0)
        self.head.next = self.tail
        self.tail.prev = self.head
        
    def get(self, key: int) -> int:
        if key in self.mp:
            node = self.mp[key]
            self._remove(node)
            self._insert(node)
            return node.val
        else:
            return -1

    def put(self, key: int, value: int) -> None:
        if key in self.mp:
            self._remove(self.mp[key])
        if len(self.mp) == self.cap:
            self._remove(self.tail.prev)
        self._insert(Node(key, value))
        
    def _remove(self, node):
        del self.mp[node.key]
        node.prev.next = node.next
        node.next.prev = node.prev
    
    def _insert (self, node):
        self.mp[node.key] = node
        head_next = self.head.next
        self.head.next = node
        node.prev = self.head
        node.next  = head_next
        head_next.prev = node
        

# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)