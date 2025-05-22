## Problem Statement

The developers at Amazon want to perform a reliability drill on some servers. There are `n` servers, each with an initial health value and capable of serving a certain number of requests.

- Each server can serve a specific number of requests.
- Every second, the developers can send the maximum number of requests that can be served by all the available servers.
- Additionally, they can send a virus to one of the servers, which decreases its health by a specified number of units `k`.
- A server goes down when its health is less than or equal to 0.
- After all the servers are down, the developers must send one more request to indicate the failure of the application.

Your task is to find the minimum total number of requests the developers need to use to bring all servers down.

---

### Input

- `request[n]`: A list where each element `request[i]` represents the number of requests that server `i` can serve.
- `health[n]`: A list where each element `health[i]` represents the initial health of server `i`.
- `k`: The amount of health that is reduced from a server's health each time a virus is sent.

---

### Output

Return a single integer representing the minimum number of requests required to bring all the servers down, including the final request to conclude the failure.

---

### Constraints:

- \( 1 \leq n \leq 10^5 \)
- \( 1 \leq \text{request}[i], \text{health}[i] \leq 5 \times 10^3 \)
- \( 1 \leq k \leq 5 \times 10^3 \)

---

### ✅ Sample Input
```python
request = [1, 2, 3]
health  = [3, 2, 1]
k = 2
```

### 📋 Execution Table

| Second | Alive Servers | Requests Sent     | Virus Target | New Healths        | Notes                          |
|--------|----------------|--------------------|----------------|---------------------|--------------------------------|
| 1      | 0, 1, 2         | 1 + 2 + 3 = 6       | Server 2       | [3, 2, -1]          | Server 2 dies (1 → -1)         |
| 2      | 0, 1            | 1 + 2 = 3           | Server 1       | [3, 0, -1]          | Server 1 dies (2 → 0)          |
| 3      | 0               | 1                   | Server 0       | [1, 0, -1]          | Server 0 health 3 → 1          |
| 4      | 0               | 1                   | Server 0       | [-1, 0, -1]         | Server 0 dies (1 → -1)         |
| —      | —               | **1**               | —              | —                   | Final request (conclude drill) |

### ✅ Total Requests

```plaintext
6 (sec 1) + 3 (sec 2) + 1 (sec 3) + 1 (sec 4) + 1 (final) = 12

```

r = [3, 4]
h = [4, 6]
k = 3


| No. of Requests | Total Requests | Virus Target | Servers' Health After |
|-----------------|----------------|--------------|------------------------|
| 3 + 4 = 7       | 7              | Server 1     | [4, 6] → [4, 3]        |
| 3 + 4 = 7       | 14             | Server 1     | [4, 3] → [4, 0] (dies) |
| 3               | 17             | Server 0     | [4] → [1]              |
| 3               | 20             | Server 0     | [1] → [-2] (dies)      |
| 1 (Final req)   | 21             | -            | All down              |


