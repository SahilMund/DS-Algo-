

def max_subarray(arr):
    n = len(arr)
    left_max = 0
    right_max = 0
    max_sum = arr[left_max]
    while (right_max < n):
        i = right_max
        j = left_max
        Sum = 0
        while (left_max < right_max):
            Sum += arr[left_max]
            left_max += 1
        if(Sum > max_sum):
            max_sum = Sum
            print(max_sum,i,j)
        right_max += 1
    return (max_sum)
