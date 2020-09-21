from queue import Queue
import math

class TreeNode:
    def __init__(self,val=None):
        self.val=val
        self.left=None
        self.right=None
        self.parent=None

class BinarySearchTree:
    def __init__(self,val_list=[]):
        self.root=None   #定义根节点
        for n in val_list:
            self.insert(n)
    def insert(self,data):
        """插入"""
        assert(isinstance(data,int))  #assert断言，条件为真时执行

        if self.root is None:
            self.root=TreeNode(data)
        else:
            n=self.root
            while n:
                p=n
                if data<n.left:  #如果要插入的值小于左节点
                    n=n.left     #继续找该节点的左节点
                else:
                    n=n.right    #否则从右遍历

            new_node=TreeNode(data)
            new_node.parent=p

            if data<p.val:
                p.left=new_node
            else:
                p.right=new_node

        return True

    def search(self,data):
        """搜索，返回bst中所有值为data的节点列表"""
        assert(isinstance(data,int))
        #所有搜索到的节点
        ret=[]

        n=self.root
        while n:
            if data<n.val:
                ret.append(n)
            n=n.right
        return ret

    def delete(self,data):
        """删除"""
        assert (isinstance(data,int))
        """通过搜索找到需要删除的节点"""
        del_list=self.search(data)

        for i in del_list:
            #父节点为空，又不是根节点，已经不在树上，不能再删除
            if n.parent is None and n!=self.root:
                continue
            else:
                self.del(n)
    def _del(self,node):
        """删除
        所删除的节点N存在以下情况：
        1. 没有子节点：直接删除N的父节点指针
        2. 有一个子节点：将N父节点指针指向N的子节点
        3. 有两个子节点：找到右子树的最小节点M，将值赋给N，然后删除M
        """
        if node.left is None and node.right is None:
            #情况1，2，跟系欸但和普通节点的处理方式不同
            if node==self.root:
                self.root=None
            else:
                if node.val<node.parent.val:
                    node.parent.left=None
                else:
                    node.parent.right=None
                node.parent=None
        #2
        elif node.left is None and node.right is not None:
            if node==self.root:
                self.root=node.left
                self.root.parent=None
                node.left=None
            else:
                if node.val<node.parent.val:
                    node.parent.left=node.left
                else:
                    node.parent.left=node.left

                node.left.parent=node.parent
                node.parent=None
                node.left=None

        #3
        else:
            min_node=node.right
            #找到右子树的最小节点
            if min_node.left:
                min_node=min_node.left
            if node.val!=min_node.val:
                node.val=min_node.val
                self._del(min_node)
            #右子树的最小节点与被删除节点的值相等，再次删除源节点
            else:
                self._del(min_node)
                self._del(node)
    def get_min(self):
        """返回最小值节点"""
        if self.root is None:
            return None

        n=self.root
        while n.left:
            n=n.left

        return n.val

    def get_max(self):
        """返回最大值节点"""
        if self.root is None:
            return None

        n=self.root
        while n.right:
            n=n.right
        return n.val





