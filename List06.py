def main(fruits):
    """
    Given a list called Fruits, it contains at least one apple. Find how many apples are on the list and return.
    Args:
        fruits(list): parameter
    Returns:
        int: return answer
    """ 
    k = fruits.count("apple")
    return k
fruits = ["apple", "banana", "apple", "pear"]
print(main(fruits))