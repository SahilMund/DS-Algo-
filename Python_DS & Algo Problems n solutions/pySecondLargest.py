def secondLargest(nums):
  nums.sort()
  max = nums[-1];
  for i in range(len(nums)):
    if(nums[-(i+1)] < max):
      return nums[-(i+1)]

def main():
  N = int(raw_input())
  if(N < 2 or N > 100):
    return
  nums = map(int , raw_input().split())
  print(secondLargest(nums))

if __name__ == '__main__':
  main()