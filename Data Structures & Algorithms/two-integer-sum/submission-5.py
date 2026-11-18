class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        output = []

        if(len(nums) == 0):
            return output
        else:
            for i in range(len(nums)):
                for j in range(i + 1, len(nums)):
                    if nums[i] + nums[j] == target:
                        return [i, j]
   
        

                


            
    