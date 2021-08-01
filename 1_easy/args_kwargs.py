# args kwargs

def super_func(*args, **kwargs):
    # args -> tuple 
    # kwargs will return a dictionary
   total = 0
   for items in kwargs.values():
       total += items
    
   return sum(args) + total

print(super_func(1,2,3,4,5, num1=5, num2=6))