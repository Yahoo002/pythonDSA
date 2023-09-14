# brute force method
# O(n^2) time complexity

# class Solution:
#     def twoSum(self, nums: list[int], target: int) -> list[int]:
#         n = len(nums)
#         for i in range(n-1):
#             for j in range(i+1, n):
#                 if nums[i] + nums[j] == target:
#                     return [i, j]
#         return []


# if __name__ == '__main__':
#     s2 = Solution()
#     print(s2.twoSum([3, 6, 9], 9))


# Hash Map method with HashTable
# time: O(n) worst time complexity if collissions exist
# time: O(1) is there are no collissions and as hash map lookups are constant
# space: O(n)
# time and space is same for both two-pass and one-pass


# two-pass hashtable

# class Solution:
#     def twoSum(self, nums: list[int], target: int) -> list[int]:
#         numMap = {}
#         n = len(nums)
#         for i in range(n):
#             numMap[nums[i]] = i
#         for i in range(n):
#             complement = target - nums[i]
#             if complement in numMap and numMap[complement] != i:
#                 return [i, numMap[complement]]

#         return []


# if __name__ == '__main__':
#     s2 = Solution()
#     print(s2.twoSum([3, 6, 9], 9))


# one-pass hashtable
# inserting and checking for complement is done at the same time (one-pass)

class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        numMap = {}
        n = len(nums)

        for i in range(n):
            complement = target - nums[i]
            if complement in numMap:
                # the last two values give the numebers which are making up the sum
                return [numMap[complement], i, complement, nums[i]]
            numMap[nums[i]] = i
        return []
# we take numMap[comeplement] before i because numMap[complement] will have the lower value first while i is still incrementing


if __name__ == '__main__':
    s2 = Solution()
    print(s2.twoSum([3, 2], 5))
