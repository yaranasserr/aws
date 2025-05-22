import heapq

def getMaxRequestStrategy(request, health, k):

    n = len(request)
    total_requests = 0
    alive = [True] * n

    while any(alive):
        # Total requests served this second
        req_this_round = sum(request[i] for i in range(n) if alive[i])
        total_requests += req_this_round

        # Build max heap based on request[i], then min health as tie-breaker
        heap = [(-request[i], health[i], i) for i in range(n) if alive[i]]
        heapq.heapify(heap)

        if heap:
            _, _, target = heapq.heappop(heap)
            health[target] -= k
            if health[target] <= 0:
                alive[target] = False

    total_requests += 1  # Final request after all servers are down
    return total_requests

# Example usage:
r = [3, 4]
h = [4, 6]
k = 3
print(getMaxRequestStrategy(r, h, k))  # Output: 21



request = [1, 2, 3]
health  = [3, 2, 1]
k = 2
print(getMaxRequestStrategy(request, health, k)) # 12
# r = [3,4]
# h =[4,6]
# k = 3
# print(getMinRequests(r, h, k)) # 21