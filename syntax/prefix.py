def create_prefix_array(nums):
    n = len(nums)
    prefix_array = [1] * n  # Step 1: Start with an array of 1s
    prefix = 1  # Step 2: Initialize prefix product

    for i in range(n):  # Step 3: Iterate through the array
        prefix_array[i] = prefix  # Store the current prefix product
        prefix = prefix * nums[i]  # Update the prefix product
        print(prefix)

    return prefix_array  # Return the final prefix array


# Example usage:
nums = [1, 2, 3, 4]
# prefix [1,1,1,1]
# nums = 1, 2 6
result = create_prefix_array(nums)
print("Prefix Array:", result)  # Output: [1, 1, 2, 6]