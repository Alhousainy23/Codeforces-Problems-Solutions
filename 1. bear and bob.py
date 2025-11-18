# Bear and Bob
a, b = map(int, input().split()) # Initial populations of bear and bob
years = 0 # Years counter
while a <= b: # While bear population is less than or equal to bob population
    a *= 3 # Bear population triples each year
    b *= 2 # Bob population doubles each year
    years += 1 # Increment years counter
print(years) # Output the number of years until bear population exceeds bob population
