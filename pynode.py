# Python program to reverse a linked list 
# Time Complexity : O(n) 
# Space Complexity : O(1) 

# Node class hevy
class Node: 

	# Constructor to initialize the node object 
	def _init_(self, data): 
		self.data = data 
		self.next = None

class LinkedList: 

	# Function to initialize head 
	def _init_(self): 
		self.head = None

	# Function to reverse the linked list 
	def reverse(self): 
		prev = None
		current = self.head 
		while(current is not None): 
			next = current.next
			current.next = prev 
			prev = current 
			current = next
		self.head = prev 
		
print "Given Linked List"
llist.printList() 
llist.reverse() 
print "\nReversed Linked List"
llist.printList() 

	# Function to insert a new node at the beginning 
	def push(self, new_data): 
		new_node = Node(new_data) 
		new_node.next = self.head 
		self.head = new_node 

	# Utility function to print the linked LinkedList 
	def printList(self): 
		temp = self.head 
		while(temp): 
			print temp.data, 
			temp = temp.next


# Driver program to test above functions 
llist = LinkedList() 
llist.push(20) 
llist.push(4) 
llist.push(15) 
llist.push(85) 

print "Given Linked List"
llist.printList() 
llist.reverse() 
print "\nReversed Linked List"
llist.printList() 
xyz=100
zyx=200
xxx=xyz+zyx
print(xxx)
print("End of the program")
