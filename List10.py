def main(lst):
    """
    A list of zeros and ones is given. Find how many ones and how many zeros there are and return to the list form.
    Args:
        list1(list): parameter
    Returns:
        list: return answer
    """
    zero_count = lst.count(0)  # Count the number of zeros
    one_count = lst.count(1)   # Count the number of ones
    counts = [zero_count, one_count]  # Create a list with zero count and one count
    return counts

# Example usage
lst = [1, 0, 0, 0, 1, 0, 1, 0]

print(main(lst))