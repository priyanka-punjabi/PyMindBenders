'''
Leetcode Question: 11. Container With Most Water
https://leetcode.com/problems/container-with-most-water/
'''
def maxarea(height):
    if len(height) < 2:
        return 0

    ptr1 = 0
    ptr2 = len(height) - 1
    max_area = 0
    while ptr1 <= ptr2:
        max_area = max(max_area, min(height[ptr1], height[ptr2]) * (ptr2 - ptr1))
        if height[ptr1] < height[ptr2]:
            ptr1 += 1
        else:
            ptr2 -= 1

    return max_area

if __name__ == '__main__':
    input = []
    input1 = [11]
    input2 = [5, 7, 4]
    input3 = [3, 0, 4, 11, 2]
    input4 = [1, 2, 3, 4, 5]
    input5 = [1, 8, 6, 2, 5, 4, 8, 3, 7]
    print(maxarea(input5))