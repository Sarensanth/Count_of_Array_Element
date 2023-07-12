def count_of_num(array):
    size=len(array)
    max=-float('inf')
    for i in array:
        if i>max:
            max=i
    count=0
    for i in array:
        if max==i:
            count+=1
    return size-count

array=list(map(int,input().split()))
print(count_of_num(array))
