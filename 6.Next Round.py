#Next Round Problem 
num_of_members,participant = map(int,input().split()) 
scores=list(map(int,input().split())) # Read all data for participent
threshold = scores[participant-1]
counting = 0 # Counting the number of participent is qualified 
for score in scores:
    if score >=threshold and score > 0 : counting+=1 # If score is greater than from threshod and greater than from 0 ==> increase counting
print(counting)