# class Solution(object):
#     def search(self, nums, target):
#         left = 0
#         right = len(nums) - 1
#         while(left<=right):
#             midle = int((left + right) / 2)
#             if nums[midle] == target:
#                 return midle
#             elif nums[midle]<target:
#                 left = midle+1
#             elif nums[midle]>target:
#                 right = midle-1
#         return -1
# sun = [-1,0,3,5,9,12]
# print(Solution().search(sun,9))

# def bubbleSort(arr):
#     n = len(arr)
#     # 遍历所有数组元素
#     for i in range(n):
#         for j in range(n - i - 1):
#             if arr[j] > arr[j + 1]:
#                 arr[j], arr[j + 1] = arr[j + 1], arr[j]
#     return arr
# arr = [64, 34, 90,25, 12, 22, 11]
#
# print(bubbleSort(arr))


















