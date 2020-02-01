from datetime import date 
  
class Test: 
    def __init__(self, name, age): 
        self.name = name 
        self.age = age 
      
    # a class method to create a  
    # Person object by birth year. 
    @classmethod
    def create(cls, name, year): 
        return cls(name, date.today().year - year) 
      
    # a static method to check if a 
    # Person is adult or not. 
    @staticmethod
    def isAdult(age): 
        return age > 18
  
test1 = Test('ads', 21) 
test2 = Test.create('ads', 1996) 
  
print (test1.age) 
print (test2.age) 
  
# print the result 
print (Test.isAdult(40)) 