**Title:** Reverse Nodes in k-Group

**Parameters:**

* **Inputs:** `head` (head node of a singly linked list), `k` (a positive integer)
* **Constraints / Requirements:** Reverse the nodes of a linked list $k$ at a time. If the number of remaining nodes at the end is less than $k$, **you must also reverse this remaining group**.

---

### Key Difference from LeetCode 25

* **LeetCode 25:** If the number of remaining nodes is less than $k$, leave them as-is (do not reverse).
* **TikTok Variant (This Problem):** If the number of remaining nodes is less than $k$, **reverse them as well**. Every group, full or partial, gets reversed.

---

### Example

* **Input:** `head = [1, 2, 3, 4, 5]`, `k = 3`
* **LeetCode 25 Output:** `[3, 2, 1, 4, 5]` *(The last 2 nodes `[4, 5]` are left untouched)*
* **This Problem's Output:** `[3, 2, 1, 5, 4]` *(The last 2 nodes `[4, 5]` are also reversed to `[5, 4]`)*