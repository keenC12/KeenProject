
start = int(input("Input start: "))
end = int(input("Input end: "))

def factor_count(n):
    
    for i in range (1,end):
        x = len([i for i in range(1,end) if not n % i]) 
        return (x)
    
#start = int(10)
#end = int(25)

count_list =[]
num_list = list(range(start,end +1))

for i in num_list:
    count_list.append(factor_count(i))
     
 
   
maxFactorPos = count_list.index(max(count_list))
number_index = num_list[maxFactorPos]

print("Number with most factors: ",number_index)
