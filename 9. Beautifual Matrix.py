#Create a matrix we are needed [5*5]
matrix = [list(map(int,input().split())) for _ in range(5)]
#Detect the location of number = 1
for i in range(5):
    for j in range(5):
        if matrix[i][j] ==1 :
            row,col = i+1,j+1
            break 
moves_counting = abs(row-3) + abs(col-3)
print(moves_counting)