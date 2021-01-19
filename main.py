def sumBetween(num1, num2):
    
    total = 0
    
    for i in range (num1 + 1, num2):
        total = total + i
    
    return total 

print(sumBetween(5,7))