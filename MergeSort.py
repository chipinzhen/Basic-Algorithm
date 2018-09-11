def MergeSort(l, left, right):
    if left >= right:
        return
    mid = left + (right - left) // 2 #注意这里的写法
    MergeSort(l, left, mid)
    MergeSort(l, mid+1, right)
    
    list_temp = list(range(len(l)))  #注意新建一个和原列表相同的长度的列表
    
    #三个指针
    pointer1 = left
    pointer2 = mid + 1
    pointer3 = left

    if (pointer1 < mid) & (pointer2 < right):
        
        if l[pointer1] < l[pointer2]:
            list_temp[pointer3] = l[pointer1]
            pointer3 += 1
            pointer1 += 1
        else:
            list_temp[pointer3] = l[pointer2]
            pointer3 += 1
            pointer2 += 1
            
    elif (pointer1 == mid) & (pointer2 < right):
        list_temp[pointer3] = l[pointer2]
        pointer3 += 1
        pointer2 += 1
    
    elif (pointer1 < mid) & (pointer2 == right):
        list_temp[pointer3] = l[pointer1]
        pointer3 += 1
        pointer1 += 1
        
    for i in range(left, right + 1):
        l[i] = list_temp[i]