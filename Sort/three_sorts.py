from typing import List


##冒泡排序
def bubble_sort(a:List[int]):
    length=len(a)
    if length<=1:
        return
    for i in range(length):
        made_swap=False
        for j in range(length-i-1):
            if a[j]>a[j+1]:
                a[j]=a[j+1]
                a[j+1]=a[j]
                made_swap=True

        if not made_swap:
            break

###插入排序
def insertion_sort(a:List[int]):
    length=len(a)
    if length<=1:
        return

    for i in range(length):
        value=a[i]
        j=i-1
        while j>=0 and a[j]>value:
            a[j+1]=a[j]
            j-=1
        a[j+1]=value

def selection_sort(a:List[int]):
    length=len(a)
    if length<=1:
        return

    for i in range(length):
        min_index=i
        min_val=a[i]

        for j in range(i,length):
            if a[j]<min_val:
                min_val=a[j]
                min_index=j
        a[i],a[min_index]=a[min_index],a[i]


def test_bublle_sort():
    test_array=[1,1,1,1]
    bubble_sort(test_array)
    assert test_array==[1,1,1,1]
    test_array=[4,1,2,5]
    bubble_sort(test_array)
    assert test_array==[1,2,3,4]
    test_array=[4,3,2,1]
    bubble_sort(test_array)
    assert test_array==[1,2,3,4]

def test_insertion_sort():
    test_array=[1,1,1,1]
    bubble_sort(test_array)
    assert test_array==[1,1,1,1]
    test_array=[4,1,2,3]
    bubble_sort(test_array)
    assert test_array==[1,2,3,4]
    test_array=[1,2,3,4]
    bubble_sort(test_array)
    assert test_array==[1,2,3,4]


def test_selection_sort():
    test_array=[1,1,1,1]
    selection_sort(test_array)
    assert test_array==[1,1,1,1]
    test_array=[4,3,2,1]
    selection_sort(test_array)
    test_array=[1,2,3,4]
    test_array=[4,3,2,1]
    selection_sort(test_array)
    assert test_array==[1,2,3,4]

if __name__ == '__main__':
    array=[4,5,8,2,1,89,45,7]
    bubble_sort(array)
    print(array)

    array=[3,5,7,9,34,2,7,0]
    insertion_sort(array)
    print(array)

    array=[2,4,6,7,3,56]
    selection_sort(array)
    print(array)