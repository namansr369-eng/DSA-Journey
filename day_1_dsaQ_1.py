# 380. Insert Delete GetRandom O(1)
# Medium

# Implement the RandomizedSet class:

# RandomizedSet() Initializes the RandomizedSet object.
# bool insert(int val) Inserts an item val into the set if not present. Returns true if the item was not present, false otherwise.
# bool remove(int val) Removes an item val from the set if present. Returns true if the item was present, false otherwise.
# int getRandom() Returns a random element from the current set of elements (it's guaranteed that at least one element exists when this method is called). Each element must have the same probability of being returned.
# You must implement the functions of the class such that each function works in average O(1) time complexity.

import random

class RandomizedSet:

    def __init__(self):
        # Stores the elements. Provides O(1) access and O(1) random choice.
        self.lst = []
        # Maps an element's value to its index in self.lst. Provides O(1) search/lookup.
        self.idx_map = {}

    def insert(self, val):
        if val in self.idx_map:
            return False

        # 1. Add value to the list.
        self.lst.append(val)
        # 2. Store its index in the map.
        self.idx_map[val] = len(self.lst) - 1
        return True

    def remove(self, val):
        if val not in self.idx_map:
            return False

        idx_to_remove = self.idx_map[val]
        last_element = self.lst[-1]

        # Optimization/Refactoring: Only perform the swap if the element
        # is NOT already the last element in the list.
        if idx_to_remove != len(self.lst) - 1:
            # 1. Move the last element to the removal position in the list.
            self.lst[idx_to_remove] = last_element
            # 2. Update the map with the new, correct index for the moved element.
            self.idx_map[last_element] = idx_to_remove

        # 3. Remove the last element from the list (it's either the duplicate or the original val).
        self.lst.pop()
        # 4. Remove the entry from the map.
        del self.idx_map[val]
        return True

    def getRandom(self):
        # Uses Python's built-in O(1) random selection on a list.
        return random.choice(self.lst)