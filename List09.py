def main(fruits):
    """
    A list called “fruits” is given and is five in length and contains at least one “apple”. Calculate how many “apple” were involved and return the indexes in a list view.
    Args:
        fruits(list): parameter
    Returns:
        list: return answer
    """
    
    i=0
    ans = []
    j = 0 
    a = 0 
    while i<=len(fruits)-1:
        if fruits[i]=="apple":
            ans.append(i)
            
        i+=1  
    k = len(ans) 
    ans.insert(0,k)        
    return ans 
fruits = ["apple", "banana", "apple", "pear", "apple"]
print(main(fruits))