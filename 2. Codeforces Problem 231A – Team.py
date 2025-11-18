# Team in codeforces Problem 231A
num = int(input()) # Number of teams
solved_count = 0 # Counter for problems solved by at least two team members
for _ in range (num): # Loop thriugh each team
    p, v, t = map(int,input().split()) # Input for each team member's solution status
    if p + v + t >=2 : # Check if at least two members solved the problem 
        solved_count +=1 # Increment the counter
print(solved_count) # Output the total count of problems solved by at least two members