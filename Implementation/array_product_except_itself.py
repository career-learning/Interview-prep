"""
Given an array nums of n integers where n > 1,  return an array output such that output[i] is equal to the product of all the elements of nums except nums[i].

Example:

Input:  [1,2,3,4]
Output: [24,12,8,6]
Constraint: It's guaranteed that the product of the elements of any prefix or suffix of the array (including the whole array) fits in a 32 bit integer.

Note: Please solve it without division and in O(n).

Follow up:
Could you solve it with constant space complexity? (The output array does not count as extra space for the purpose of space complexity analysis.)
"""


class Solution:
    def productExceptSelf(self, nums):
        """
        1. do we have duplicated values?
        2. can we cache the result? 

        k = [] , input = [1,2,3,4]
        result = []


        for i in input:
            x = input.pop[i]
            result.append(product(input))
            k.append(x)

        iteration  

        0     x=1  input=[2,3,4]  result=[24]                                       k=[1]
        1     x=2. input=[3,4]    result=[24,pruduct(k)*product(input)]             k=[1,2]             
        2     x=3  input=[4]      result= [24,12,product(k)*product(input), ]       k=[1,2,3]   
        3     x=4  input=[]       result= [24,12,8, product(k)*product(input)]      k=[1,2,3,4]
        """

        low = 1  # prod of integers before i
        high = 1  # product of integers after n-1-i
        n = len(nums)
        result = [1]*n  # [1,1,1,1]
        result[0] = 1
        for i in range(1, n):
            # [1,1,2,6]
            result[i] = result[i-1] * nums[i-1]

        for i in range(n-1, -1, -1):
            #  [1*24,1*12,2*4,6*1]
            result[i] *= high
            high *= nums[i]

        return result
        # result = [i+1 * i+2*...., i-1*i+1*i+2..., i-2*i-1*i+1.. ]
