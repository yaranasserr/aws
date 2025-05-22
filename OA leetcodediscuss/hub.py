# https://leetcode.com/discuss/post/6669696/amazon-oa-question-by-anonymous_user-6e9t/
def precompute_next_hub(sorted_hubs, n):
    next_hub = [-1] * n
    # Fill the next_hub array in reverse order
    last_hub = sorted_hubs[-1]
    for i in range(n - 2, -1, -1):
        if i in sorted_hubs:
            last_hub = i
        next_hub[i] = last_hub
    return next_hub

def compute_hub_costs(points, queries):
    n = len(points)
    results = []
    
    # Precompute the next hub for each index
    for query in queries:
        hubs = set(idx - 1 for idx in query)  # Convert to 0-based
        hubs.add(n - 1)  # Always include the last point as hub
        sorted_hubs = sorted(hubs)

        # Precompute next hub index for each point
        next_hub = precompute_next_hub(sorted_hubs, n)
        
        total_cost = 0
        for i in range(n):
            if i in hubs:
                continue  # skip hub

            next_hub_idx = next_hub[i]
            if next_hub_idx != -1:
                total_cost += points[next_hub_idx] - points[i]

        results.append(total_cost)

    return results



points = [1, 3, 5, 8]
queries = [[1, 3], [2, 4]]

print(compute_hub_costs(points, queries))  # Output: [2, 5]
