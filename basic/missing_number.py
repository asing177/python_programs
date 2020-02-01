def find_missing(lst): 
    return [i for x, y in zip(lst, lst[1:])  
        for i in range(x + 1, y) if y - x > 1] 
  
# Driver code 
lst = [1, 2, 4, 6, 7, 9, 10] 
print(find_missing(lst)) 




def find_missing(lst): 
    return sorted(set(range(lst[0], lst[-1])) - set(lst)) 
  
# Driver code 
lst = [1, 2, 4, 6, 7, 9, 10] 
print(find_missing(lst)) 



def find_missing(lst): 
    start = lst[0] 
    end = lst[-1] 
    return sorted(set(range(start, end + 1)).difference(lst)) 
  
# Driver code 
lst = [1, 2, 4, 6, 7, 9, 10] 
print(find_missing(lst)) 