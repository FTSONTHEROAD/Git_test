def permute(nums):
    # 如果列表为空，返回空列表
    if not nums:
        return [[]]

    permutations = []
    for i in range(len(nums)):
        # 递归获取除当前元素外的其余元素的全排列
        rest_permutations = permute(nums[:i] + nums[i + 1:])
        # 将当前元素与其余元素的全排列合并
        for perm in rest_permutations:
            permutations.append([nums[i]] + perm)
    return permutations


# 测试代码
nums = [1, 2, 3]
result = permute(nums)
for perm in result:
    print(perm)
