'''
Leetcode Question: 1. Two Sum
https://leetcode.com/problems/two-sum/
Time Complexity: O(n)
Space Complexity: O(n)
'''
def twoSum(nums, target):
    if len(nums) < 2:
        return None

    tracker = dict()
    for i in range(len(nums)):
        if abs(target - nums[i] in tracker):
            return [tracker[target - nums[i]], i]
        tracker[nums[i]] = i

    return None

if __name__ == '__main__':
    target = 11
    input = []
    input1 = [11]
    input2 = [5, 7, 4] # [1,2]
    input3 = [3, 0, 4, 11, 2] # [1,3]
    input4 = [1, 2, 3, 4, 5] # null
    print(defcall(input4, target))