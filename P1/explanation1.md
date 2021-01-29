explanation1.md

Problem1 :
+ Least Recently Used Cache is the program where we remove the least recently used item from when the limit is reached.
+ I have used OrderedDict datastructure as it keep the dictionay item in order, and I am adding new item at the ends
+ time-complexity : O(1) as it is always entering value at the end of OrderedDict, space complexity : O(n)

Problem2 :
+ Code to find file with .c extension in directory and subdirectory using file recursion
+ I have used list datastructure to add the new found path, as list datastructure doesn't have a limit in size.
+ time-complexity : theta(n) using recurrence relation, https://yourbasic.org/algorithms/time-complexity-recursive-functions/ , space complexity O(n)

Problem 3:
+ HuffmanCoding to encode and decode a string using a simple PriorityQueue and binary tree. It encodes left with 0 and right with 1
+ I have used PriorityQueue and BinaryTree datastructure, as HuffmanCoding is based on that ..
+ time-complexity: O(nlogn) , space complexity  is O(k) for tree and O(n) for decoded text

Problem 4:
+ Active Directory, note: I have implemented it as such that it will check user inside all the group ..
+ I have used list datastructure for groups and user list in the active directory
+ time-complexity: O(n) , space complexity O(n)

Problem 5:
+ LinkedList of Blocks to create a blockchain. Using SHA to encrypt the last block and gmt time
+ Create and used LinkedList datastructure to create blockchains
+ time-complexity : O(n), space complexity O(n)

Problem 6:
+ Using Union and Intersection on two linkedlist, note: there are no duplicate value in the new set created ..
+ I have created and used LinkedList datastructure to create union and intersection
+ time-complexity of union is O(n^2) and intersection is O(n^3), space complexity: O(n)
