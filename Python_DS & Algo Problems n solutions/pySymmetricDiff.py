# Output the symmetric difference integers in ascending order, one per line.
# 4
# 2 4 5 9
# 4
# 2 4 11 12
# Sample Output
# 5
# 9
# 11
# 12

if __name__ == '__main__':
  l1 = int(raw_input())
  nums1 = map(int, raw_input().split())
  l2 = int(raw_input())
  nums2 = map(int, raw_input().split())

  set1 = set(nums1)
  set2 = set(nums2)
  intersection = set1.intersection(set2)
  union = set1.union(set2)
  diff = union.difference(intersection)
  sdiff = sorted(diff)
  for d in sdiff:
    print(d)