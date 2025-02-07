'''
Leetcode Question: 42. Trapping Rain Water
https://leetcode.com/problems/trapping-rain-water/

Step 1: Identify the pointer with lesser value.
Step 2: Is this pointer greater than or equal to the max on that side?
If yes -> We update the max on that side.
If no -> We get the water for that pointer and add to total.
Step 3: Move the pointer inward.
Step 4: Repeat until all pointers are traversed.

Time Complexity: O(n)
Space Complexity: O(1)
'''

def trapRainWater(height):
    ptr1 = 0
    ptr2 = len(height) - 1
    max_left = max_right = total_water = 0
    while ptr1 < ptr2:
        if height[ptr1] <= height[ptr2]:
            if height[ptr1] >= max_left:
                max_left = height[ptr1]
            else:
                total_water += max_left - height[ptr1]
            ptr1 += 1
        else:
            if height[ptr2] >= max_right:
                max_right = height[ptr2]
            else:
                total_water += max_right - height[ptr2]
            ptr2 -= 1

    return total_water

if __name__ == "__main__":
    input = [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]
    input1 = [0, 1, 0, 2, 1, 0, 3, 1, 0, 1, 2]
    print(trapRainWater(input))