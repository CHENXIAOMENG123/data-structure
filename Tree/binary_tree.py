'''二叉树的遍历'''

'''前序遍历'''
from  typing import TypeVar,Generic,Generator,Optional

T=TypeVar("T")

class TreeNode(Generic[T]):
    def __init__(self,value:T):
        self.val=value
        self.left=None
        self.right=None

    def pre_order(root:Optional[TreeNode][T])->Generator[T,None,None]:
        if root:
            yield root.val  #显示节点数据
            yield from pre_order(root.left)  #先遍历左子树
            yield from pre_order(root.right)  #再遍历右子树

    def in_order(root:Optional[TreeNode][T])->Generator[T,None,None]:
        if root:
            yield from in_order(root.left)
            yield root.val
            yield from in_order(root.right)

    def post_order(root:Optional[TreeNode][T])-> Generator[T,None,None]:
        if root:
            yield from post_order(root.left)
            yield from post_order(root.right)
            yield root.val

if __name__ == '__main__':
    singer=TreeNode("taylor swift")

    genre_country=TreeNode("love story")
