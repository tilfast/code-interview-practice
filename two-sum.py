def twoSum(nums, target) -> list:
    hashmap = {}
    for idx, n in enumerate(nums):
        hashmap[idx] = n
        try:
            comp_idx = list(hashmap.keys())[list(hashmap.values()).index(target - n)]
            if comp_idx == idx:
                comp_idx = 0
                continue
            return [comp_idx, idx]
        except Exception as e:
            continue


test = [2, 7, 11, 15]
print(test)
print(twoSum(test, 9))
print(9)
print(twoSum(test, 18))
print(18)
print(twoSum(test, 13))
print(13)

test = [3, 2, 4]
print(twoSum(test, 6))
print(6)
