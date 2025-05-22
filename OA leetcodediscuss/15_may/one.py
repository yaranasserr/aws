#https://leetcode.com/discuss/post/6748124/recent-amazon-oa-questions-by-anonymous_-zqu0/
# The data engineers at Amazon are working on partitioning their server chains. There is a linear chain of n servers numbered from 1 to n,
# where the cost parameter associated with the ith server is represented by the array cost[i]. These servers need to be partitioned into exactly k 
# different server chains. The cost of partitioning a server chain servers[i: j] is defined as cost[i] + cost[j].
# The total cost is the sum of the partitioning cost of each server chain.

# Given n servers, an array cost and an integer k, find the minimum and maximum possible total cost 
# of the operations and return them in the form of an array of size 2: [minimum cost, maximum cost].

# Note: Partitioning of an array means splitting the array sequentially into two or more parts where 
# each element belongs to exactly one partition. For an array [1, 2, 3, 4, 5], a valid partition would be 
# [[1], [2, 3], [4, 5]], while [[1, 2], [2, 3], [4, 5]] and [[1, 3], [2, 4, 5]] would be considered invalid partitions.

from typing import List

def find_partition_cost(arr: List[int], k: int) -> List[int]:
    cost_of_partitions = []
    
    # Calculate the cost of each partition (arr[i-1] + arr[i])
    for i in range(1, len(arr)):
        cost_of_partitions.append(arr[i - 1] + arr[i])
    
    # Sort the partition costs
    cost_of_partitions.sort()
    
    ends = arr[0] + arr[-1]
    
    # Calculate min cost: smallest k-1 partitions + ends
    min_cost = ends + sum(cost_of_partitions[:k - 1])
    
    # Calculate max cost: largest k-1 partitions + ends
    max_cost = ends + sum(cost_of_partitions[-(k - 1):])
    
    return [min_cost, max_cost]
