def negative_numbers(start, end):
    """
    Function to return all negative numbers in a given range.

    Args:
    start (int): Start of the range.
    end (int): End of the range.

    Returns:
    list: List of negative numbers in the given range.
    """
    # Create a list comprehension to find negative numbers
    negatives = [i for i in range(start, end + 1) if i < 0]
    
    # Return the list of negative numbers
    return negatives

# Test the function
start_range = -4
end_range = 5
negative_nums = negative_numbers(start_range, end_range)
print("Negative numbers in the range:", negative_nums)
