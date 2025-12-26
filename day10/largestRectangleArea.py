def largestRectangleArea(heights):
    n = len(heights)
    max_area = 0
    
    # For each bar, try to expand left and right
    for i in range(n):
        height = heights[i]
        left = i
        right = i
        
        # Expand to left
        while left > 0 and heights[left-1] >= height:
            left -= 1
        
        # Expand to right
        while right < n-1 and heights[right+1] >= height:
            right += 1
        
        # Calculate area
        width = right - left + 1
        area = height * width
        max_area = max(max_area, area)
    
    return max_area

# Example usage
heights = [2,1,5,6,2,3]
print("Largest Rectangle Area:", largestRectangleArea(heights))
