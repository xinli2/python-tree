"""
    File: tree_funcs.py
    Author: Xin Li
    Purpose: In this program, i will implement a varity of other
    functions.This~
"""
def count(root):
    #return the number of node in the tree.
    if root is None:
        return 0
    else:
        return count(root.get_left()) + count(root.get_right())+1
def is_bst(root):
    '''
        return true if the tree is a BST,empty tree and single note.
        False if not.
    '''

    if (count(root)==0) or (count(root)==1):
        return True

    if root.get_left() != None:
        is_bst(root.get_left())
    if root.get_right() != None:
        is_bst(root.get_right())
    if root.get_left() < root.get_val():
        return True
    if root.get_right() < root.get_val():
        return True
    else:
        return False
    if  root_left != None and max( root_left) > root_val:
               return false;
    if  root_left != None and min( root_left) < root_val:
               return false;
    if is_bst( root_left)==True or is_bst( root_right)==True:
               return  false;
'''
    search the tree for the given value. If it is found,
    returns the node which contains the value; otherwise,
    return None.
'''
def search(root, val):
    if root.get_val() == None:
        return None
    if root.get_val() == val:
        return root
    node = None
    if root.get_right() is not None:
        node = search(root.get_right(), val)
    if node is not None :
        return node
    if root.get_left() is not None:
        node = search(root.get_left(), val)
    return node
def bst_search(root,val):
    if root.get_val() == None:
        return None
    if root.get_val() == val:
        return root
    node = None
    if root.get_right() is not None:
        node = search(root.get_right(), val)
    if node is not None :
        return node
    if root.get_left() is not None:
        node = search(root.get_left(), val)
    return node
'''
    return a traversal of the values in the tree; the return
    value from this function must be an array containing the
    values (not the nodes). An empty tree should return an
    empty list.
'''
array1 = []
def pre_order_traversal(root):
    if root:
        array1.append(root.val)
        pre_order_traversal(root.left)
        pre_order_traversal(root.right)
    return array1
array2 = []
def post_order_traversal(root):
    if root:
        post_order_traversal(root.left)
        post_order_traversal(root.right)
        array2.append(root.val)
    return array2
array3=[]
def in_order_traversal(root):
    if root:
        in_order_traversal(root.left)
        array3.append(root.val) ,
        in_order_traversal(root.right)
    return array3
