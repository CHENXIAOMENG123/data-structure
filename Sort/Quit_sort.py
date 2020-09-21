#分治思想实现快速排序算法

#如果要排序数组中下标从 p 到 r 之间的一组数据，我们选择 p 到 r 之间的任意一个数据作为 pivot（分区点）。
# 我们遍历 p 到 r 之间的数据，将小于 pivot 的放到左边，将大于 pivot 的放到右边，将 pivot 放到中间。
# 经过这一步骤之后，数组 p 到 r 之间的数据就被分成了三个部分，
# 前面 p 到 q-1 之间都是小于 pivot 的，中间是 pivot，后面的 q+1 到 r 之间是大于 pivot 的。

from typing import List
import random

def quick_sort(a:List[int]):
    _quick_sort_between(a,0,len(a)-1)

def _quick_sort_between(a:List[int],low:int,high:int):
    if low<high:
        #获取一个随机位置的数作为分区点（pivot）
        k=random.randint(low,high)
        a[low],a[k]=a[k],a[low]

        m=_partition(a,low,high)
        #a[m]是最后一个元素
        _quick_sort_between(a,low,m-1)
        _quick_sort_between(a,m+1,high)


def _partition(a:List[int],low:int,high:int):
    pivot,j=a[low],low
    for i in range(low+1,high+1):
        if a[i]<=pivot:
            j+=1
            a[j],a[i]=a[i],a[j]
    a[low],a[j]=a[j],a[low]
    return j


def test_quick_sort():
    a1=[3,5,6,7,8]
    quick_sort(a1)
    assert a1==[3,5,6,7,8]

if __name__ == '__main__':
    a1=[3,5,6,7,8]
    quick_sort(a1)
    print(a1)




