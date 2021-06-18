#Cycle detection in linked list
#Time complexity O(N) space complexity O(1)
#Floy Cycle detection
def CycleDetection(head):
	if(head==None or head.next==None or head.next.next == None): 
		return None

	slow = head.next
	fast = head.next.next

	#determinate if there is a cycle if the pointers find each other
	while (slow != fast):
		if(fast.next == None or fast.next.next == None):
			return None
		slow = slow.next
		fast = fast.next

	#if a cycle is detected, restart slow to determinate where the cycle start
	slow = head
	while(slow != fast):
		slow=slow.next
		fast=fast.next
	return slow