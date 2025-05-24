### **Problem Statement: Minimize Total Variation**

As an operations engineer at Amazon, you are responsible for organizing the distribution of `n` different items in the warehouse. The size of each product is given in an array `productSize`, where `productSize[i]` represents the size of the *i-th* product.

You are to construct a new array called `variation`, where each element `variation[i]` is defined as the difference between the largest and smallest product sizes among the first `i + 1` products. Mathematically:

```
variation[i] = max(productSize[0..i]) - min(productSize[0..i])
```

Your goal is to **reorder** the products to **minimize the total variation**, defined as:

```
Total Variation = variation[0] + variation[1] + ... + variation[n - 1]
```

Write a function that returns the **minimum possible total variation** after reordering the array.

---

### **Function Signature**

```python
def minimizeVariation(productSize: List[int]) -> int:
```

---

### **Input**

* An integer array `productSize` of length `n`, where:

  * `1 ≤ n ≤ 2000`
  * `1 ≤ productSize[i] ≤ 10^9`

---

### **Output**

* An integer: the minimum total variation after optimally reordering the array.

---

### **Example**

#### **Input**

```python
productSize = [3, 1, 2]
```

#### **Output**

```python
3
```

#### **Explanation**

By reordering the array as `[2, 3, 1]`:

* `variation[0] = max(2) - min(2) = 0`
* `variation[1] = max(2, 3) - min(2, 3) = 1`
* `variation[2] = max(2, 3, 1) - min(2, 3, 1) = 2`

Total variation = `0 + 1 + 2 = 3`, which is the minimum possible.

---

### **Sample Input 0**

```
productSize = [4, 5, 4, 6, 2, 1, 1]
```

### **Sample Output 0**

```
16
```

### **Explanation**

After sorting: `[1, 1, 2, 4, 4, 5, 6]`

* `variation[0] = 0`
* `variation[1] = 0`
* `variation[2] = 1`
* `variation[3] = 3`
* `variation[4] = 3`
* `variation[5] = 4`
* `variation[6] = 5`

Total = `0 + 0 + 1 + 3 + 3 + 4 + 5 = 16`

---

### **Sample Input 1**

```
productSize = [6, 1, 4, 2]
```

### **Sample Output 1**

```
9
```

### **Explanation**

After sorting: `[1, 2, 4, 6]`

* `variation[0] = 0`
* `variation[1] = 1`
* `variation[2] = 3`
* `variation[3] = 5`

Total = `0 + 1 + 3 + 5 = 9`

---


