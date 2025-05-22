## Problem Statement

Each delivery zone is represented as an interval `(a, b)` indicating the range of house numbers it covers. These delivery zones can **overlap**.

You are given a list of existing delivery zones, where each zone covers an inclusive interval `[a, b]`. Additionally, you are given an integer `k` — the **maximum allowed length** of any new delivery zone that can be added, i.e., `b - a <= k`.

Your task is to **add exactly one** new delivery zone `[a, b]` such that the new zone satisfies the length constraint, and after adding it, the **total number of disconnected delivery regions** is minimized.

---

## Definition of Connected Zones

A set of delivery zones is said to be **connected** if **every house number in the range from the minimum to the maximum house number** is covered by **at least one** of the delivery zones in that set.

### Example:

- The set `[(1,5), (2,4)]` is **connected** because all house numbers from `1` to `5` are covered.
- The set `[(2,2), (3,4)]` is **not connected**, because there’s a gap between `2` and `3`.

---

## Example

Given delivery zones:

intervals = [(1,5), (2,4), (6,6), (7,14), (16,19)]  
k = 2

If you add the new delivery zone `[5,7]`, the zones can be grouped into two connected sets:

[(1,5), (2,4), (5,7), (6,6), (7,14)]  
[(16,19)]

This results in **2 connected delivery sets**.

However, if you instead add `[14,16]`, the zones are grouped into:

[(1,5), (2,4)]  
[(6,6)]  
[(7,14), (14,16), (16,19)]

Which results in **3 connected sets**, which is worse.

Hence, the optimal new delivery zone is `[5,7]` and the minimum number of connected delivery sets is **2**.

---

## Input

- Two integer arrays `start[]` and `end[]` of length `n` representing the start and end of each existing delivery zone.
- An integer `k`, the **maximum allowed length** of the new delivery zone.

---

## Output

- Return an **integer** denoting the **minimum number of connected delivery regions** after adding one new delivery zone of length at most `k`.
