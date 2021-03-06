'''
问题描述：
一个序列有N个数：A[1],A[2],…,A[N]，求出最长非降子序列的长度。
(讲DP基本都会讲到的一个问题LIS：longest increasing subsequence)

思路：
假如我们考虑求A[1],A[2],…,A[i]的最长非降子序列的长度，其中i<N， 那么上面的问题变成了原问题的一个子问题(问题规模变小了，你可以让i=1,2,3等来分析)
然后我们定义d(i)，表示前i个数中以A[i]结尾的最长非降子序列的长度。
如果我们把d(1)到d(N)都计算出来，那么最终我们要找的答案就是这里面最大的那个。
OK，状态找到了，下一步找出状态转移方程。

可以举个例子，然后求出前面几项，找出递推规律
d(i)可以用下面的状态转移方程得到：
d(i) = max{1, d(j)+1},其中j<i,A[j]<=A[i]
'''

def LIS(A):
    d = [0 for i in range(len(A))]
    for i in range(len(A)):
        d[i] = 1   # 就算前面所有元素都比当前大，那么至少可以包含自身，所以长度默认值为1
        for j in range(i):
            if A[i] >= A[j] and d[j]+1 > d[i]:
                d[i] = d[j] + 1
    return max(d)

A = [5, 3, 4, 8, 6, 7]
print(LIS(A))
