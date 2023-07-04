def main(fruits):
    """
    A list called "fruits" is given and is five in length and contains at least one "apple". Remove the apples from the list and return the list.
    Args:
        fruits(list): parameter
    Returns:
        list: return answer
    """
    i=0
    while i<=len(fruits)-1:
        if fruits[i]=="apple":
            fruits.remove(fruits[i])
        i+=1
    return  fruits
fruits = ["apple", "banana", "apple", "pear", "apple"]
print(main(fruits))