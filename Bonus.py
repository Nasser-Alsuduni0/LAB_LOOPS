n= int(input("Enter a positive integer:"))
number_range = range(1 , n+1)
num = 0
for number in number_range:
    if number % 2 == 0 :
        num += number 
print(num)    
     

