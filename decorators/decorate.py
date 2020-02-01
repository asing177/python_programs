def decorator(func): 
    def inner_func(): 
        print("Before Decoration") 
        func() 
        print("After Decoration")  
    return inner_func 
  
  

def to_be_decorated(): 
    print("Inside the function !!") 
  
decorated = decorator(to_be_decorated) 
decorated() 