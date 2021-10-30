"""
    File: tree_node.py
    Author: Xin Li
    Purpose: In this program, i will delcare the class TreeNode.
    The TreeNode class represents a single node in a binarY tree.
    This class may be used to represent either a search tree or
    an unordered tree . If this is a BST, then it is the
    reponsibility of the "outside" code to make sure that it only
    uses BST-compatible functions.
"""
class TreeNode:
    def __init__(self,val):
        self._left = None
        self._right = None
        self._value = val
    def get_left(self):
        return self._left
    def get_right(self):
        return self._right
    def get_val(self):
        return self._value
    def set_left(self,left):
        self._left = left
    def set_right(self,right):
        self._right = right
    def search(self,val):
        if self._value == None:
            return False
        if self._value == val:
            return self
        node = None
        if self._right is not None:
            node = self._right.search(val)
        if node is not None :
            return node
        if self._left is not None:
            node = self._left.search(val)
        return node
    def bst_search_loop(self,val):
        if self._value == None:
            return False
        node = self
        while node is not None:
            if node._value == val:
                return node
            elif node._value > val:
                node = node._left
            elif node._value < val:
                node = node._right
        if node is None:
            return None
    def bst_insert_loop(self,val):
        if self._value == val:
            return "NOP"
        node = self
        tree_node = TreeNode(val)
        while node is not None:
            if val < node._value :
                if node._left is not None:
                    node = node._left
                else:
                    node._left = tree_node
                    return
            if node._value < val :
                if node._right is not None:
                    node = node._right
                else:
                    node._right = tree_node
                    return
        return
