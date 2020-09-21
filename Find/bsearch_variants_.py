'''二分查找的四种变形形式'''
'''查找第一个值等于给定值的元素'''
'''查找最后一个值等于给定值的元素'''
'''查找最后一个小于等于给定值的元素'''

'''前半部分操作一致'''
from typing import List

'''找第一个相同的值'''

def bsearch_LEFT(nums:List[int],target:int):
    low,high=0,len(nums)-1
    while low<=high:
        mid=low+(high-low)//2
        '''如果中间值小于目标值，则从后半段找，即low是后半段的起始点'''
        '''反之从前半段开始寻找，high变成前半段最大值'''
        if nums[mid]<target:
            low=mid+1
        else:
            high=mid-1
        '''low从0开始，找到第一个符合的值就返回了'''
        if low<len(nums) and nums[low]==target:
            return low
        else:
            return -1

'''找到和目标值相同的最后一个值'''

def bsearch_right(nums:List[int],target:int):
    low,high=0,len(nums)-1

    while low<high:
        mid=low+(high-low)//2
        if nums[mid]>target:
            high=mid-1
        else:
            low=mid+1

        '''只要high还在范围内，就一直往后找，直到num【high】=target'''
        if high>0 and nums[high]==target:
            return high
        else:
            return -1

'''查找第一个大于等于给定值的元素'''

def bsearch_left_not_less(nums:List[int],target):
    low,high=0,len(nums)-1

    while low<high:
        mid=low+(high-low)//2
        if nums[mid]>target:
            high=mid-1
        else:
            low=mid+1

        ''''''
        if low<len(nums) and nums[low]>=target:
            return low
        else:
            return -1

'''查找最后一个小于等于给定值的元素'''

def bsearch_right_not_less(nums:List[int],target):
    low,high=0,len(nums)-1

    while low<high:
        mid=low+(high-low)//2
        if nums[mid]>target:
            high=mid-1
        else:
            low=mid+1

        ''''''
        if high<len(nums) and nums[high]<=target:
            return high
        else:
            return -1

if __name__ == '__main__':
    a=[1,1,2,3,4,5,7,8,8,8,8,9]

    print(bsearch_LEFT(a,0))

'''有序数列反转后找target
'''
def search(nums:List[int],target:int):

    while left <=right:
                mid = left+(right-left)//2
                if nums[mid] == target:
                    return mid
                if nums[left] <= nums[mid]:
                    if nums[left] <= target < nums[mid]:
                        right = mid - 1
                    else:
                        left = mid + 1
                elif nums[mid] <= nums[right]:
                    if nums[mid] < target <= nums[right]:
                        left = mid + 1
                    else:
                        right = mid - 1
                    return -1
