class Solution:
    def fizzBuzz(self, n):
        list = []
        for i in range(1, n+1):
            if i % 5 == 0 and i % 3 == 0:
                string = "FizzBuzz"
            elif i % 5 == 0:
                string = "Buzz"
                
            elif i % 3 == 0:
                string = "Fizz"
                
            else:
                string = str(i)
            
            list.append(string)
            
        return list
        
