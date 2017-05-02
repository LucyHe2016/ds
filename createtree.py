# create a tree based on two traverse order
# preorder, inorder

class TreeNode:

    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

def create_tree(preorder, inorder):
    node = TreeNode(preorder[0])

    index_in_inorder = inorder.index(preorder[0])
    if index_in_inorder == 0:
        node.left = None
    else:    
        node.left = create_tree(preorder[1:index_in_inorder+1], inorder[:index_in_inorder])

    if index_in_inorder+1 == len(preorder):
        node.right = None
    else:
        node.right = create_tree(preorder[index_in_inorder+1:], inorder[index_in_inorder+1:])

    return node

def post_traverse(t, f):
    if t is not None:
        post_traverse(t.left, f)
        post_traverse(t.right, f)
        f(t.value)

if __name__ == '__main__':
    preorder = [4, 3, 1, 2, 8, 7, 16, 10, 9, 14]
    postorder = [1, 2, 3, 4, 7, 8, 9, 10, 14, 16]
    t = create_tree(preorder, postorder)
    post_traverse(t, print)
