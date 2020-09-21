#归并排序

from typing import List

def merge_sort(a:List[int]):
    _merge_sort_between(a,0,len(a)-1)

#用递归实现
#
def _merge_sort_between(a:List[int],low:int,high:int):
    if low<high:
        mid=low+(high-low)//2
        _merge_sort_between(a,low,mid)  #分成两组
        _merge_sort_between(a,mid+1,high)
        _merge(a,low,mid,high)  #将数组合并为有序数组

def _merge(a:List[int],low:int,mid:int,high:int):
    #a[low:mid],a{mid:high],are sorted

    #两个游标，一个指向前半部分对一个元素一个指向后半部分的第一个元素
    i,j=low,mid+1
    tmp=[]  #临时数组，大小和A相同
    while i<=mid and j<=high:
        #比较两个元素，如果A[I]<=A[j]，把小的放到临时数组中，再把临时数组拷贝到原数组中，
        #并且i后移一位
        if a[i]<=a[j]:   #
            tmp.append(a[i])
            i+=1
        else:
            tmp.append(a[j])
            j+=1

        #循环以上过程，知道其中一个子数组的所有数据都放在了临时数组中
        #再把另一个数组中的数据加入到临时数组的末位，此时临时数组储存了两个数组合并的结果
    start=i if i <=mid else j
    end=mid if i <=mid else high
    tmp.extend(a[start:end +1])
    a[low:high+1]=tmp  #把临时数组拷贝到原数组


def test_merge_sort():
    a1=[3,5,6,7,8]
    merge_sort(a1)
    assert a1==[3,5,6,7,8]
    a2=[2,2,2,2]
    merge_sort(a2)
    assert a2==[2,2,2,2]
    a3=[4,3,2,1]
    merge_sort(a3)
    assert a3==[1,2,3,4]

if __name__ == '__main__':
    a1=[3,5,6,7,8]
    a2=[2,2,2,2]
    a3=[4,3,2,1]
    merge_sort(a1)
    print(a1)
    merge_sort(a2)
    print(a2)
    merge_sort(a3)
    print(a3)



