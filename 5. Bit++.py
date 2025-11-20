#Bit Problem 
num_of_operations = int(input())
x = 0
for i in range (num_of_operations):
    instructions = input()
    if '++' in instructions: x+=1
    else : x-=1
print(x)