'''
SESSION 22 (25/10/2023)
Mentor and Facilitator ==> ANDY AFFUL

TITLE: Implement a Queue Data Structure

PROBLEM STATEMENT: Queues are crucial data structures in computer science and have various real-world
applications. One of the practical scenarios where queues are essential is managing tasks in a printer spooler
system.Consider a printer spooler system where multiple users send print requests to a shared printer.
The printer processes these requests in the order they are received, following the FIFO principle.
Create your own queue data structure in Python where the element that is added first will be the first one
to be removed.

Your queue should support the following methods:
- enqueue(element): Add an element to the back of the queue.
- dequeue(): Remove and return the element from the front of the queue. If the queue is empty, return None.
- peek(): Return the element at the front of the queue without removing it. If the queue is empty, return None.
- is_empty(): Return True if the queue is empty; otherwise, return False.
- size(): Return the number of elements in the queue.

class MyQueue:
    def __init__(self):
        # Initialize the queue as an empty list.
        self.queue = []

    def enqueue(self, element):
        # Implement the enqueue method.
        pass

    def dequeue(self):
        # Implement the dequeue method.
        pass

    def peek(self):
        # Implement the peek method.
        pass

    def size(self):
        # Implement the size method.
        pass

    def is_empty(self):
        # Implement the is_empty method.
        pass

# Example Usage:
my_queue = MyQueue()
my_queue.enqueue(1)
my_queue.enqueue(2)
my_queue.enqueue(3)
print(my_queue.size())  # Should print 3 since there are 3 element in the queue
print(my_queue.dequeue())  # Should print 1
print(my_queue.peek())     # Should print 2
print(my_queue.is_empty()) # Should print False
'''
# SOLUTION 1
class MyQueue:
    def __init__(self):
        self.queue = [] #queue initaialized as an empty list

    #method to add element to the back of the queue
    def enqueue(self, element):
        self.queue.append(element)
