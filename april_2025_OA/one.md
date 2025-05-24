## Q1: Lexicographically Maximal Package Sorting

Amazon's fulfillment centers handle packages of various weights, and they need to optimize their sorting process.

Given an array `weight` which denotes the weights of `n` packages, the goal is to create the **lexicographically maximal resulting array sorted by non-increasing order of weight** using the following operations:

### Allowed Operations:

1. **Discard** the first package from the current `weight` array.
2. **Add** the first element to the resulting array, then remove it along with the next `k` (a fixed constant) elements from the current array.

> **Note:** Operation 2 can also be applied when fewer than `k` elements remain after the current element; in that case, the entire remaining array is removed.

The resulting array must have packages arranged in **non-increasing weight order**.

---

### Objective

Given an array `weight` of size `n` and an integer `k`, find the **lexicographically maximal resulting array** sorted by **non-increasing order of weight** that can be obtained.

---

### Lexicographical Order Clarification

An array `x` is lexicographically greater than an array `y` if:

- `x[i] > y[i]`, where `i` is the first position where `x` and `y` differ, **or**
- `/x/ > /y/` and `y` is a prefix of `x` (where `/x/` denotes the size of array `x`)

---

### Example 1

**Input:**
```
k = 1
n = 5
weight = [4, 3, 5, 5, 3]
```

To obtain the lexicographically maximal resulting array sorted in non-increasing order, we apply the operations accordingly.

---

### Sample Input 0 (STDIN format)


```
weight = [10, 5, 9, 2, 5]
k = 2 
```

**Sample Output 0:**
```
10  
5
```

---

### Sample Input 1


```
weight = [3]
k = 0 
```

**Sample Output 1:**
```
3
```

**Explanation:**

In this case, since there is only 1 element, we apply **Operation 2**, adding `weight[0] = 3` to the resulting array. This gives the lexicographically maximal array sorted in non-increasing order of weight.
