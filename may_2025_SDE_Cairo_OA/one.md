### Problem Statement

The engineering team at an Amazon fulfillment center is optimizing n high-performance printers, where each printer can print pages[i] number of pages.

Each printer can be in exactly one of three states: operational, idle, or suspended.

Printers initially start in an idle state and can be activated one by one.

However, if too many printers are active at once, some will get suspended due to their threshold limit defined by the suspension rule below.

---

### Suspension Rule

If there are at least x operational printers, all such printers with threshold[i] < x will get suspended and stop printing.

---

### Task

The goal is to determine the maximum number of pages that can be printed before printers get suspended.

**Note:**

Activating a printer with threshold[i] = x allows it to print pages[i] pages. However, once at least x printers are active, their pages get printed first, and then all the printers with threshold ≤ x will get suspended immediately.

Choosing the activation order carefully is therefore crucial to maximize the total printed pages before suspensions occur.

---

### Example

**n = 4**  
**pages = [2, 6, 10, 13]**  
**threshold = [2, 1, 1, 1]**

The optimal way to maximize the number of pages printed is as follows (using 1-based indexing):

1. First, the engineers decide to activate the 4th printer, which prints 13 pages. At this point, the total number of operational printers is 1. The printing of 13 pages is completed first, followed by the suspension of any printers exceeding their threshold.

2. Next, since the threshold for printers 2, 3, and 4 is 1, and there is now 1 operational printer (4th printer), these printers become damaged. Thus, all the printers (2nd, 3rd, and 4th) with threshold = 1 get suspended and stop functioning.

3. Next, the only printer the team can turn on is printer 1. By activating printer 1, they print 2 more pages. The number of operational printers is now 1, and because threshold[1] = 2, printer 1 will not be suspended and remains functional.

**Total printed pages = 13 (from printer 4) + 2 (from printer 1) = 15**

Hence, the answer is **15**.

---

### Function Description

Complete the function `getPages` in the editor below.

```python
def getPages(pages: List[int], threshold: List[int]) -> int:
    # your code here
```

#### Parameters:

- `pages[n]`: number of pages that printers can print
- `threshold[n]`: threshold values of printers

#### Returns:

- `long`: Maximum number of pages that you can print.

---

### Constraints

- 1 ≤ n ≤ 2×10⁵  
- 1 ≤ threshold[i] < n  
- 1 ≤ pages[i] < 10⁹  

---

### Input Format For Custom Testing

#### Sample Case 0

##### Input:

```
5
4
1
5
2
3
5
3
3
233
```

##### Function

```
pages[] size n = 5
pages = [4, 1, 5, 2, 3]
threshold[] size n = 5
threshold = [3, 3, 2, 3, 3]
```

##### Output:

```
14
```

---

### Explanation

The optimal way to maximize the number of pages printed is as follows (1-based indexing):

1. Turn on the 4th printer, which prints 2 pages. Since the number of operational printers is 1 and does not exceed the threshold for any printer, no printer is suspended.

2. Next, turn on the 3rd printer, which prints 5 pages. Now, there are 2 operational printers. Since the threshold for printer 3 is threshold[3] = 2, printer 3 gets suspended and stops functioning. So, now we have only 1 operational printer which is the 4th one.

3. Turn on the 1st printer, which prints 4 pages. There are now 2 operational printers, and printer 1 remains functional as its threshold is threshold[1] = 3.

4. Finally, turn on the 5th printer, which prints 3 pages. Now, there are 3 operational printers (printers 1, 4, and 5). Since the thresholds for printers 1, 2, 4, and 5 are all less than or equal to 3, these printers get suspended and stop functioning.

**Total printed pages = 2 (from printer 4) + 5 (from printer 3) + 4 (from printer 1) + 3 (from printer 5) = 14 pages**

Hence, the answer is **14**.

---

### Sample Case 1

##### Input:

```
6
2
4
4
4
5
3
```

##### Function

```
pages[] size n = 6
pages = [2, 4, 4, 4, 5, 3]
threshold[] size n = 6
threshold = [1, 3, 1, 3, 3, 2]
```

##### Output:

```
20
```

---

### Explanation

The optimal way to maximize the number of pages printed is as follows (1-based indexing):

1. Turn on the 3rd printer, which prints 4 pages. At this point, since there is 1 operational printer and the thresholds for printers 1 and 3 are 1, both printers 1 and 3 get suspended and stop functioning. So, now we have 0 operational printers.

2. Next, turn on the 2nd printer, which prints 4 pages. No printers are suspended since the number of operational printers (equal to 1) is within the threshold.

3. Turn on the 6th printer, which prints 3 pages. Operational printers become equal to 2. Printer 6 gets suspended and stops functioning because its threshold is 2. Now there is only 1 operational printer (2nd printer).

4. Turn on the 4th printer, which prints 4 pages. Number of operational printers becomes equal to 2.

5. Finally, turn on the 5th printer, which prints 5 pages. Now, printers 2, 4, and 5 get suspended and stop functioning since there are 3 operational printers, and their thresholds are less than or equal to 3.

**Total printed pages = 4 (from printer 3) + 4 (from printer 2) + 3 (from printer 6) + 4 (from printer 4) + 5 (from printer 5) = 20 pages**

Hence, the answer is **20**.
