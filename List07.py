def main(list1):
    """
    A list of zeros and ones is given. Find how many zeros are involved and return.
    Args:
        list01(list): parameter
    Returns:
        int: return answer
    """
    k = list1.count(0)
    return k
list1 = [1, 0, 1, 1, 0, 1, 1]
print(main(list1))