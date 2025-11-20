# Boy Girl Problem 
username = input()
#Calculate the number of characters by used a set 
distinct_chars = set(username)
#Validating to the number of chars if it's odd or even 
if len(distinct_chars)%2==0: print("CHAT WITH HER!")
else : print("IGNORE HIM!")