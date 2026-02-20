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
import copy

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
# A heap is:
# A complete binary tree stored inside an array.
#       1
#      / \
#     5  10
# Smallest element always at root.
# import heapq
# heap = []
# heapq.heappush(heap, 5)
# heapq.heappush(heap, 1)
# heapq.heappush(heap, 15)
# heapq.heappop(heap)
# print(heap[0])
# print(heap)

# Core_Exercises
# 1️⃣ Reverse a String
# userInput = "hello"
# if len(userInput)>0:
#     print(userInput[::-1])
# else:
#     print("")

# 2️⃣ Check Palindrome
# At first mismatch → it is NOT a palindrome.
# Input= "racecars"
# # Using two pointers
# left=0
# right=len(Input) -1
# is_pal = True
# if(len(Input)==0): print("True")
# while(left<right):
#      if(Input[left]!=Input[right]):
#          is_pal = False
#          break
#      left+=1
#      right-=1
# print(is_pal)

# 3️⃣ Two Sum
# pointers technique
# nums = [2,7,11,15]
# l=0
# r=len(nums)-1
# sum=0
# target = 18
# while(l<r):
#     sum=nums[l]+nums[r]
#     if(target<sum):
#         r-=1
#     elif(target>sum):
#         l+=1
#     elif(target==sum):
#         print(l,r)
#         break

# 4️⃣ Count Duplicates
# frequency hashing
# Input= [1,2,3,2,4,1,1]
# freq={}
# count=0
# for i in Input:
#     freq[i]=freq.get(i,0)+1
# for i in freq.values():
#     if i>1:
#         count+=1
# print(count)

# 5️⃣ Rotate List
# from collections import deque
# nums = deque([1,2])
# k = 3
# nums.rotate(k)
# print(nums)

# 7️⃣ Merge Two Sorted Lists
# Input1= [1,3,5]
# Input2= [2,4,6]
# i = j = 0
# merged = []
# while i < len(Input1) and j < len(Input2):
#     if Input1[i] < Input2[j]:
#         merged.append(Input1[i])
#         i += 1
#     else:
#         merged.append(Input2[j])
#         j += 1
# merged.extend(Input1[i:])
# merged.extend(Input2[j:])


# 8️⃣ Remove Duplicates
# Input= [1,2,2,3,4,4,5]
# freq={}
# list1=[]
# for i in Input:
#     freq[i]=freq.get(i,0)+1
# for i,x in freq.items():
#     if x>1:
#         list1.append(i)
# print(list1)



# 9️⃣ Find Missing Number
# Input= [9,6,4,2,3,5,7,0,1]
# n=len(Input)
# expected=n*(n+1)//2
# actual=sum([num for num in Input])
# print(expected-actual)

# 🔟 Anagram Check
# Input1= "listen"
# Input2= "silent"
# freq1={}
# for i in Input1:
#     freq1[i]=freq1.get(i,0)+1
# freq2={}
# for i in Input2:
#     freq2[i]=freq2.get(i,0)+1
#
# if(freq1==freq2):
#     print("True")
# else:
#     print("False")
# Order never matters in dictionary

# Drill
# import copy
# a = [1, 2, 3]
# b = a              # reference (same object)
# c = a.copy()       # shallow copy (new list object)
# d = copy.copy(a)   # shallow copy (same as a.copy for list)
# print("a:", a, "id:", id(a))
# print("b:", b, "id:", id(b))
# print("c:", c, "id:", id(c))
# print("d:", d, "id:", id(d))

# unsorted two sum(hashmap)
# nums = [2,7,11,15]
# target = 9
# def two_sum(nums, target):
#   seen={}
#   for i,num in enumerate(nums):
#       diff=target-num
#       if diff in seen:
#           return (seen[diff],i)
#       seen[num]=i
# print(two_sum([2,7,11,15],9))
# nums=[1,2,2,3,4,4,5]
# def find_duplicates(nums):
#     freq={}
#     store=[]
#     for i in nums:
#         freq[i]=freq.get(i,0)+1
#     for i,num in freq.items():
#         if num > 1:
#             store.append(i)
#     return store
# print(find_duplicates(nums))


# def merge_sorted(a, b):
#     i=j=0
#     merge=[]
#     while i < len(a) and j < len(b):
#         if a[i]<b[j]:
#             merge.append(a[i])
#             i+=1
#         else:
#             merge.append(b[j])
#             j+=1
#     merge.extend(a[i:])
#     merge.extend(b[j:])
#     return merge
# a=[2,4,5]
# b=[1,3,6]
# print(merge_sorted(a,b))

# Sliding window
# nums = [2,1,5,1,3,2]
# k=3
# # have to find max sum with range k in nums range
# def max_subarray_sum(nums, k):
#     if k <= 0: return "k Must be Positive Numbers"
#     if k>len(nums): return "K is larger than nums"
#     window_sum=sum(nums[:k])
#     max_sum=window_sum
#     for right in range(k,len(nums)):
#         window_sum+=nums[right]
#         window_sum-=nums[right-k]
#         if max_sum<window_sum:
#             max_sum = window_sum
#     return max_sum
# print(max_subarray_sum(nums,k))

