## Log Analysis

### Problem
You are given a log file containing entries in the following format:
timestamp,user_id,action

Example:
10:01,user1,login
10:03,user2,search
10:05,user1,purchase
10:07,user2,search
10:10,user3,login


The task is to compute:
- **Most Active User** (user with the highest number of actions)
- **Most Common Action**

---

## Algorithm

1. Read the log file **line by line** to avoid loading the entire dataset into memory.
2. Use two **hash maps (dictionaries)**:
   - One to count **user activity**
   - One to count **action frequency**
3. For each log entry:
   - Split the line using `,` to extract `timestamp`, `user_id`, and `action`.
   - Increment the count of the corresponding `user_id`.
   - Increment the count of the corresponding `action`.
4. After processing the entire file:
   - Find the user with the **highest action count**.
   - Find the action with the **highest frequency**.
5. Output the **most active user** and **most common action**.

---

## Data Structures Used

### Hash Map (`user_count`)

Stores the number of actions performed by each user.

Example:
{
"user1": 2,
"user2": 2,
"user3": 1
}


### Hash Map (`action_count`)

Stores the frequency of each action.

Example:
{
"login": 2,
"search": 2,
"purchase": 1
}


### Why Dictionaries?

- **O(1) average lookup and update**
- Efficient for **counting and aggregation**
- Works well for **large datasets**

---

## Complexity Analysis

**Time Complexity:**  
`O(N)`  
Each log entry is processed exactly once.

**Space Complexity:**  
`O(U + A)`

Where:
- `U` = number of unique users
- `A` = number of unique actions

---

## Handling Large Log Files Efficiently

The program processes the file **line by line** instead of loading the entire file into memory.  
This ensures that very large log files can be processed efficiently while keeping memory usage low.

Only the **aggregated counts** (users and actions) are stored in memory.
