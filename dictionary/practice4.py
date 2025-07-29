nums = list(map(int,input("Nhập các số nguyên cách nhau dấu cách: ").split()))
target = int(input("nhập target: "))

def two_sum(nums, target):
    phan_tu = {}
    for i in range (len(nums)):

        complement = target - nums[i]

        if complement in phan_tu:
            return [phan_tu[complement], i]
        phan_tu[nums[i]] = i
    return []



print (nums)

print (two_sum(nums, target))

