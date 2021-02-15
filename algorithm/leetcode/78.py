from itertools import combinations

# class Solution:
#     def subsets(self, nums: List[int]) -> List[List[int]]:
#         answer=[]
#         for i in range(len(nums)+1):
#             answer.extend(combinations(nums,i))
#         return answer
# class Solution:
#     def subsets(self, nums: List[int]) -> List[List[int]]:
#         n = len(nums)
#         output = [[]]
        
#         for num in nums:
#             output += [curr + [num] for curr in output]
        
#         return output
n = len([1,2,3])
nums=[1,2,3]
output = []

for i in range(2**n, 2**(n + 1)):
    print(i)
    # generate bitmask, from 0..00 to 1..11
    bitmask = bin(i)[3:]
    print(bitmask)
    # append subset corresponding to that bitmask
    output.append([nums[j] for j in range(n) if bitmask[j] == '1'])

print(output)