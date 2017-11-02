# https://github.com/nryoung/algorithms/blob/master/algorithms/data_structures/binary_search_tree.py

class Node(object):
    def __init__(self, key=None, val=None, size_of_subtree=1):
        self.key = key # Key
        self.val = val # Value
        self.size_of_subtree = size_of_subtree
        self.left = None
        self.right = None
        
class BinarySearchTree(object):
    def __init__(self):
        self.root = None
        
    def _size(self, node):
        if node in None:
            return 0
        else:
            return node.size_of_subtree

    def size(self):
        '''
        Return the nubmer of nodes.
        Worst Case: O(1)
        Balanced Tree Complexity: O(1)
        '''
        return self._size(self.root)
    
    def is_empty(self):
        '''
        Worst Case: O(1)
        Balanced Tree Complexity: O(1)
        '''
        return self.size() == 0
    
    def _get(self, key, node):
        if node is None:
            return None
        
        if key < node.key:
            return self._get(key, node.left)
        elif key > node.key:
            return self._get(key, node.right)
        else:
            return node.val
        
    def get(self, key):
        """
        Return the value using key
        Worst Case: O(N)
        Balanced Tree Complexity: O(log(N))
        """
        return self._get(key, self.root)
         
    def contains(self, key):
        """
        Return Boolean whether the tree contains key.
        Worst Case Complexity: O(N)
        Balanced Tree Complexity: O(log(N))
        """
        return self.get(key) is not None
    
    def _put(self, key, val, node):
        if node is None:
            return Node(key, val) # If root is empty, Create Node.

        if key < node.key:
            node.left = self._put(key, val, node.left)
        elif key > node.key:
            node.right = self._put(key, val, node.right)
        else: # if key == node.key: overwight value.
            node.val = val
            
        node.size_of_subtree = self._size(node.left) + self._size(node.right) + 1 # ??
        return node
        
    def put(self, key, val):
        """
        Add new key & value.
        Worst Case Complexity: O(N)
        Balanced Tree Complexity: O(log(N))
        """
        self.root = self._put(key, val, self.root)
        
    def _min_node(self):
        """
        Return the node with the minimum key
        """
        min_node = self.root
        
        if min_node is None: # If root in None, return None.
            return None 
        
        while min_node.left is not None:
            min_node = min_node.left
            
        return min_node
        
     
    def min_key(self):
        """
        Return the minimum key
        Worst Case Complexity: O(N)
        Balanced Tree Complexity: O(log(N))
        """
        min_node = self._min_node()
        if min_node is None: # If root in None, return None.
            return None
        else:
            return min_node.key
        
    def _max_node(self):
        """
        Return the node with the maximum key.
        """
        max_node = self.root
        if max_node is None: # If root in None, return None.
            return None

        while max_node.right is not None:
            max_node = max_node.right

        return max_node

    def max_key(self):
        """
        Return the maximum key.
        Worst Case Complexity: O(N)
        Balanced Tree Complexity: O(log(N))
        """
        max_node = self._max_node()
        if max_node is None: # If root in None, return None.
            return None
        else:
            return max_node.key
        
    def _floor_node(self, key, node): # ???
        """
        Returns the node with the biggest key that is less than or equal to the
        given value 'key'
        """
        if node is None:
            return None

        if key < node.key:
            # Floor must be in left subtree
            return self._floor_node(key, node.left)

        elif key > node.key:
            # Floor is either in right subtree or is this node
            attempt_in_right = self._floor_node(key, node.right)
            if attempt_in_right is None:
                return node
            else:
                return attempt_in_right

        else:
            # Keys are equal so floor is node with this key
            return node

    def floor_key(self, key): # ???
        """
        Returns the biggest key that is less than or equal to the given value
        'key'
        지정된 값 'key'보다 작거나 같은 가장 큰 키를 리턴합니다.
        Worst Case Complexity: O(N)
        Balanced Tree Complexity: O(lg N)
        """
        floor_node = self._floor_node(key, self.root)
        if floor_node is None:
            return None
        else:
            return floor_node.key

    def _ceiling_node(self, key, node): # ???
        """
        Returns the node with the smallest key that is greater than or equal to
        the given value 'key'
        """
        if node is None:
            return None

        if key < node.key:
            # Ceiling is either in left subtree or is this node
            attempt_in_left = self._ceiling_node(key, node.left)
            if attempt_in_left is None:
                return node
            else:
                return attempt_in_left
        elif key > node.key:
            # Ceiling must be in right subtree
            return self._ceiling_node(key, node.right)
        else:
            # Keys are equal so ceiling is node with this key
            return node

    def ceiling_key(self, key): # ???
        """
        Returns the smallest key that is greater than or equal to the given
        value 'key'
        Worst Case Complexity: O(N)
        Balanced Tree Complexity: O(lg N)
        """
        ceiling_node = self._ceiling_node(key, self.root)
        if ceiling_node is None:
            return None
        else:
            return ceiling_node.key
        
        
        
        
        
        
        