#20260806
#https://algo.monster/liteproblems/381
import random
from typing import Set, List, Dict

class RandomizedCollection:
    def __init__(self):
        """
        Initialize your data structure here.
        """
        # Dictionary mapping values to sets of their indices in the list
        self.value_to_indices: Dict[int, Set[int]] = {}
        # List storing all values (allows duplicates)
        self.values_list: List[int] = []

    def insert(self, val: int) -> bool:
        """
        Inserts a value to the collection. Returns true if the collection did not already contain the specified element.
        """
        # Get the set of indices for this value, or create empty set if not exists
        indices_set = self.value_to_indices.get(val, set())
      
        # Add the new index (which will be at the end of the list)
        indices_set.add(len(self.values_list))
      
        # Update the mapping
        self.value_to_indices[val] = indices_set
      
        # Append the value to the list
        self.values_list.append(val)
      
        # Return True if this was the first occurrence of the value
        return len(indices_set) == 1

    def remove(self, val: int) -> bool:
        """
        Removes a value from the collection. Returns true if the collection contained the specified element.
        """
        # Check if value exists in the collection
        if val not in self.value_to_indices:
            return False
      
        # Get the set of indices for the value to remove
        indices_set = self.value_to_indices[val]#获得val的所有在数组中的位置
      
        # Get any index of the value to remove (convert set to list and take first)
        index_to_remove = list(indices_set)[0]#在数组中要挪走的元素对应的索引
      
        # Get the last index in the list
        last_index = len(self.values_list) - 1
      
        # Swap the element to remove with the last element🔥确保了从数组中remove 是O(1)
        self.values_list[index_to_remove] = self.values_list[last_index]
      
        # Remove the index from the set of the value being removed
        indices_set.remove(index_to_remove)
      
        # Update indices for the value that was swapped from the end
        last_value_indices = self.value_to_indices[self.values_list[last_index]]
      
        # Remove the old last index from the swapped value's index set
        if last_index in last_value_indices:
            last_value_indices.remove(last_index)
      
        # If we didn't remove the last element, add the new index for the swapped value
        if index_to_remove < last_index:
            last_value_indices.add(index_to_remove)
      
        # If no more indices for the removed value, delete it from the mapping
        if not indices_set:
            self.value_to_indices.pop(val)
      
        # Remove the last element from the list
        self.values_list.pop()
      
        return True

    def getRandom(self) -> int:
        """
        Get a random element from the collection.
        """
        # Return -1 if empty, otherwise return a random element
        return -1 if len(self.values_list) == 0 else random.choice(self.values_list)#O（1）


# Your RandomizedCollection object will be instantiated and called as such:
# obj = RandomizedCollection()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()
