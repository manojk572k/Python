# 1️⃣ List (Dynamic Array).)(contiguous memory) 0(1)
# a = [1, 2, 3]
# print(a)
# Operations
# print(a[1]) 0(1)
# a.append(4) 0(1)
# a.pop() 0(1)
# a.insert(0,10) 0(n)
# a.pop(2) 0(n)
# print(a)

# 2️⃣Tuple (Immutable Array)0(1)
# a = (1, 2, 3)
# a.append(4)
# print(a)
# Cannot modify
# Faster than list
# Hashable (can be dictionary key)
# When to Use
# Fixed data
# Dictionary keys
# Protect data from modification

# 3️⃣ Set (Hash Table) unoredered collection
# s = {1, 2, 3}
# u = {4,5,6}
# Operations
# s.add(20) 0(1)
# s.remove(3) 0(1)
# s.update(u). 0(k)
# print(u)
# When to Use
# Fast membership testing
# Remove duplicates
# Set operations (union, intersection)

# 4️⃣ Dictionary (Hash Map)
# d = {"name": "Manoj", "age": 24}
# d["skill"] = "Full stack Developer" 
# Here Updatation is same as insertion
# print(d.get("age")) 0(1)
# del d["age"] 0(1)
# print(d)
# print(d.keys()) 0(1)
# 🔹 When to Use
# Fast lookup by key
# Caching
# Counting frequency

# 5️⃣ Deque (Double Ended Queue)
# from collections import deque
# e=[4,5,6]
# d = deque([1,2,3])
# print(d)
# Core operations
# d.append(4) 0(1)
# d.appendleft(4)
# deque([4, 1, 2, 3])
# d.pop() 0(1)
# d.popleft() 0(1)
# d.remove(3) 0(1)
# len(d) 0(1)
# d.extend([4,5,6]) adds multiple elements from from right 0(1)
# d.extendleft([-2,-1,0]) add in right but in reverse order 0(k)
# d.rotate(2) rotates to left
# deque([2, 3, 1])
# print(d.count(1)) returns number of occurance of a value 0(n)
# d.clear() removes all elements 0(n)
# print(d[-3]) # indexing
# d.insert(2,200) (n)
# print(d)
# 🔹 When to Use
# Implementing queue (FIFO)
# BFS
# Sliding window maximum
# Monotonic queue
# Task scheduling
# LRU logic (basic)

# 6️⃣ Stack (LIFO) 0(1)
# stack=[1,2,3,4]
# operations
# stack.append(5)
# stack.pop()
# stack.remove(3)
# print(stack)

# 7️⃣ Queue (FIFO)
# best case use Deque

# 8️⃣ Heap (Priority Queue)
# import heapq
# heap = []
# heapq.heappush(heap, 5)
# heapq.heappop(heap)