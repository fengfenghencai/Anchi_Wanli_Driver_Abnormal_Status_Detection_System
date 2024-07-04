s = 15
nums = [2, 3, 1, 2, 4, 3]
n = len(nums)
left = 0
ans = n+1
summ = 0
if sum(nums) < s:
    print(0)
else:
    for right in range(n):
        summ += nums[right]
        while summ >= s and left <= right:
            summ -= nums[left]
            ans = min(ans, right-left+1)
            left += 1
    print(ans)

