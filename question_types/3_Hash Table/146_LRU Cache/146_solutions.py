#20260806
class Node:
    """Doubly linked list node for LRU Cache implementation."""
  
    def __init__(self, key: int = 0, value: int = 0) -> None:
        """
        Initialize a node with key-value pair.
      
        Args:
            key: The key for cache lookup
            value: The value associated with the key
        """
        self.key = key
        self.value = value
        self.prev: Node | None = None
        self.next: Node | None = None


class LRUCache:
    """
    Least Recently Used (LRU) Cache implementation.
  
    Uses a combination of HashMap and Doubly Linked List for O(1) operations.
    Most recently used items are kept at the head of the list.
    Least recently used items are at the tail and get evicted when capacity is exceeded.
    """
  
    def __init__(self, capacity: int) -> None:
        """
        Initialize the LRU cache with given capacity.
      
        Args:
            capacity: Maximum number of key-value pairs the cache can hold
        """
        self.capacity = capacity
        self.size = 0
        self.cache: dict[int, Node] = {}  # HashMap for O(1) lookup
      
        # Create dummy head and tail nodes to simplify edge cases
        self.head = Node()  # Dummy head node
        self.tail = Node()  # Dummy tail node
      
        # Connect dummy nodes
        self.head.next = self.tail
        self.tail.prev = self.head

    def get(self, key: int) -> int:
        """
        Get the value of the key if it exists in the cache.
        Move the accessed node to head (mark as most recently used).
      
        Args:
            key: The key to look up
          
        Returns:
            The value associated with the key, or -1 if not found
        """
        if key not in self.cache:
            return -1
      
        # Move the accessed node to head (most recently used)
        node = self.cache[key]
        self._remove_node(node)
        self._add_to_head(node)
      
        return node.value

    def put(self, key: int, value: int) -> None:
        """
        Add or update a key-value pair in the cache.
        If key exists, update its value and move to head.
        If adding new key exceeds capacity, remove least recently used item.
      
        Args:
            key: The key to add or update
            value: The value to associate with the key
        """
        if key in self.cache:
            # Update existing node
            node = self.cache[key]
            self._remove_node(node)
            node.value = value
            self._add_to_head(node)
        else:
            # Create new node
            new_node = Node(key, value)
            self.cache[key] = new_node
            self._add_to_head(new_node)
            self.size += 1
          
            # Check if capacity is exceeded
            if self.size > self.capacity:
                # Remove least recently used node (tail.prev)
                lru_node = self.tail.prev
                self.cache.pop(lru_node.key)
                self._remove_node(lru_node)
                self.size -= 1

    def _remove_node(self, node: Node) -> None:
        """
        Remove a node from its current position in the doubly linked list.
      
        Args:
            node: The node to remove from the list
        """
        # Connect the previous and next nodes directly
        node.prev.next = node.next
        node.next.prev = node.prev

    def _add_to_head(self, node: Node) -> None:
        """
        Add a node right after the dummy head (mark as most recently used).
      
        Args:
            node: The node to add to the head of the list
        """
        # Insert node between head and head.next
        node.next = self.head.next
        node.prev = self.head
        self.head.next = node
        node.next.prev = node


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
