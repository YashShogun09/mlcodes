from itertools import permutations


dist = [
    [0, 10, 15, 20],  
    [10, 0, 35, 25],   
    [15, 35, 0, 30],   
    [20, 25, 30, 0]    
]

def tsp_brute_force(dist):
    n = len(dist)
    cities = list(range(n))
    min_path = None
    min_cost = float('inf')

    for perm in permutations(cities[1:]):
        path = [0] + list(perm) + [0] 
        cost = sum(dist[path[i]][path[i+1]] for i in range(n))
        
        if cost < min_cost:
            min_cost = cost
            min_path = path

    return min_path, min_cost

path, cost = tsp_brute_force(dist)

print("🗺️ Shortest path:", ' -> '.join(map(str, path)))
print("🧮 Minimum cost:", cost)
