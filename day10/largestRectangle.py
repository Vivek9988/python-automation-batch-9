def largestRectangleArea(heights):
    stack = []          # Stack to store indexes of histogram bars
    max_area = 0        # Variable to store the maximum rectangle area
    n = len(heights)    # Total number of bars

    # Traverse through all bars
    for i in range(n):
        # If current bar is smaller than the bar at top of stack
        # then calculate area of rectangle with stack top as height
        while stack and heights[i] < heights[stack[-1]]:
            height = heights[stack.pop()]     # Height of the rectangle
            # Width is current index if stack is empty,
            # otherwise difference between current index and index after stack top
            width = i if not stack else i - stack[-1] - 1
            max_area = max(max_area, height * width)  # Update maximum area

        stack.append(i)   # Push current bar index into stack

    # Calculate area for remaining bars in stack
    while stack:
        height = heights[stack.pop()]         # Height of the rectangle
        # Width extends till the end of histogram
        width = n if not stack else n - stack[-1] - 1
        max_area = max(max_area, height * width)  # Update maximum area

    return max_area      # Return the largest rectangle area


# USER INPUT
n = int(input("Enter number of bars: "))   # Read number of bars
heights = list(map(int, input("Enter bar heights: ").split()))  # Read bar heights

# Print the result
print("Largest Rectangle Area:", largestRectangleArea(heights))