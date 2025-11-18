# Bob and Friendship
num1 , num2 = map(int,input().split())# Input two numbers
adj = [[] for _ in range (num1 + 1)] # Adjacency list for the graph
for _ in range (num2): # Loop through the number of edges
    u,v = map (int, input().split()) # Input each edge
    adj[u].append(v) # Add edge to adjacency list
    adj[v].append(u) # Add edge to adjacency list
visited = [False] * (num1 + 1 ) # Visited list to track visited nodes
is_click = True # Flag to check if all components are cliques
for i in range (1,num1 + 1): # Loop through each node
    if not visited[i]: # If the node is not visited
        component_nodes = [] # List to store nodes in the current component
        q = [i] # Queue for BFS
        visited[i] = True # Mark the node as visited
        head = 0 # Head pointer for the queue
        while head < len(q): # BFS traversal
            u = q[head] # Current node
            head += 1 # Move head pointer
            component_nodes.append(u) # Add node to component list
            for v in adj[u]: # Loop through adjacent nodes
                if not visited[v]: # If adjacent node is not visited
                    visited[v] = True # Mark it as visited
                    q.append(v) # Add it to the queue
        num_nodes = len(component_nodes) # Number of nodes in the component
        if num_nodes > 1: # If more than one node in the component
            for node in component_nodes: # Check each node in the component
                if len(adj[node]) != num_nodes - 1: # Check if it's a clique
                    is_click = False # Not a clique
                    break
        if not is_click: # If not a clique, break out of the loop
            break
if is_click: # If all components are cliques
    print ("YES") # Print YES
else: # If any component is not a clique
    print ("NO") # Print NO 