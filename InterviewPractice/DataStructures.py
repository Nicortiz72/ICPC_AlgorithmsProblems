#Queue
from collections import deque
queue = deque()
queue.append(s)
queue.popleft()

#Heap Priority queue
import heapq as hq
Heap=list()
hq.heappop(Heap)#smallest item
hq.heappush(Heap,v)

#Note: If you change all sings + to -, there is a max heap
Algorithm		Average	    Worst case
Space		     O(n)	       O(n)
Search			 O(n)	       O(n)
Insert		     O(1)	       O(log n)
Find-min		 O(1)	       O(1)
Delete-min		 O(log n)	   O(log n)


Python data structures complexity
#https://wiki.python.org/moin/TimeComplexity

#search tree
search   O(log n)   O(n)
Insert   O(log n)   O(n)
delete = search
#You can force avarage with a balance search tree


#Red–black tree


#Segment tree



https://www.ics.uci.edu/~brgallar/week8_2.html


#graphs
Adjacency matrix
Edge lists
Adjacency lists
directed graphs
undirected graphs


https://www.educative.io/blog/python-interview-questions
sorting problems
https://medium.com/@verdi/intermediate-sorting-algorithms-merge-quick-and-radix-sort-539686c5063b