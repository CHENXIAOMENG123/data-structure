import  random

def QuickSort(arr):
    #双向排序，提高非随机输入的性能
    #不需要额外的空间，再待排序数组本身内部进行排序
    #基准值通过random随机选取
    #入参：待排序数组，数组开始索引为0，数组结束索引为len（array）-1

    if arr is None or len(arr)<1:
        return arr

    def swap(arr,low,upper):
        tmp=arr[low]
        arr[low]=arr[upper]
        arr[upper]=tmp
        return arr

    def QuickSort_twoway(arr,low,upper):
        #小数组排序i可以用插入或选择排序
        #ifupper-low<50:return arr
        #基线体哦见：low index=upper index,也就是只有一个值的区间
        if low>=upper:
            return arr
        #随机选取基准值，并将基准值替换到数组的第一个元素

        swap(arr,low,int(random.uniform(low,upper)))
        temp=arr[low]

        #缓存边界值，从上下边界同时排序
        i,j=low,upper
        while True:
            #第一个元素是基准值，跳过
            i+=1
            #在小区间中，进行排序
            #从下边界开始寻找大于基准值的索引
            while i<=upper and arr[i]<=temp:
                i+=1

            #从上边界开始寻找小于基准值的索引
            #因为j肯定大于i，所以索引值肯定在小区间中

            while arr[j]>temp:
                j-=1

            if i>=j:
                break
            swap(arr,i,j)

        swap(arr,low,j)
        QuickSort_twoway(arr,low,j-1)
        QuickSort_twoway(arr, j+1,upper)
        return arr
    return QuickSort_twoway(arr,0,len(arr)-1)

if __name__ == '__main__':
    a1=[3,4,9,0,7,8]
    QuickSort(a1)
    print(a1)

