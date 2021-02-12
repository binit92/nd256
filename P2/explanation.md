
Problem1 - implementation of square Root
The square root algorithm is implemented using binary search where the value is divided by half in each step of the iteration by calculating the middle point of the range of value .
timecomplexity = O(log(n))


Problem2- search rotated sorted array
There is a pivot point in the input array from which sorting order reverses. The implementation is as such that first we find the pivot point usign binary_search and then to search actualy value, we can rely on the pivot point to search it in the right direction.
time-complexity of binary_search is O(logn)


Problem3- Rearrange array elements
First of all, the algorithms sort the input array in increasing order using the merge-sort algorithm.
Later since the array is sorted, it becomes very easy to determine the output by enumerating it in one go
time-complexity of merge-sort : O(nlogn) (overall time-complexity)


Problem-4 dutch nation flag
The input array consists of values in the set (0,1 and 2), that is being sorted in single traversal by putting
0s at the start and 2s at the end of the array. 1s will automatically be placed in between
time-complexity : O(n)



Problem-5 - Building a Trie in python
This is implementation of Trie datastructure in Jupyter Notebook that insert the word and finds the node which represents the prefix.
time-complexity : O(n)


Problem-6 - find the maximum and minimum value in a unsorted array..
It traverse the array single time and keep track of the biggest and smallest value of it. At the end these values are returned.
time-complexity : O(n)
space-complexity: O(1)


Problem-7 - httprouter-using-trie
explanation:  This is impelementation of HTTPRouter using Trie datastructure. The implementation is divided into three class RouteTrie, RouteTrieNode and Router.
RouteTrie - inserts() function inserts the node. Find() function search the Trie datastructure and return and handler .
RouteTrieNode- uses dictionary to save value, a reference to next node and a handler.
Router- has the root handler, lookup() method to find the handler from parents or paths.
method: add_handler
time-complexity: O(n), as it is looped through each value in the path
space-complexity: O(n), for every value in the path, a new TrieNode is created.
method: lookup
time-complexity: O(n), as it is looped through each value.
space-complexity: O(1), no additional memory used.
