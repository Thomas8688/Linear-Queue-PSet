#Class created to implement the linear queue data structure
class linQueue:
#Initialisation
    def __init__(self,size):
        print ("Creating Queue...")
#If the input for queue size is not an integer, the queue size will be set to a default 10
#Otherwise the queue size will be set to the users input
        if isinstance(size, int):
            self.__size = size
        else:
            self.__size = 10
            print("Invalid Queue Size: Set to Default (10)")
#Sets the queue to a list of size: self.__size with each piece of data being a null value "-"
        self.__queue = ["-" for i in range(self.__size)]
#Sets the pointers to -1 (Indexing starts at 0, so this can indicate whether or not the queue is empty)
        self.__headP = -1
        self.__tailP = -1
        print ("Queue Created\n")

#Method used to enqueue an item
    def enqueue(self, item):
#Checks if the item is a string (Required Input)
        if isinstance(item, str):
#If this is the first value being added to the queue, then both the head and tail pointers are set to point to the first list index
            if self.isEmpty():
                self.__headP = 0
                self.__tailP = 0
                self.__queue[self.__tailP] = item
                print(item, "Enqueued\n")
#Otherwise, if there are already items in the queue, then the item is added to the end of the queue, and the tail pointer is increased by 1.
            elif not self.isFull():
                self.__tailP += 1
                self.__queue[self.__tailP] = item
                print(item, "Enqueued\n")
            else:
                print("Queue is full:", item, "can not be Enqueued\n")
        else:
            print("Invalid item: not a string\n")

#Method used to Dequeue an items
    def dequeue(self):
#Checks if the queue is empty
        if not self.isEmpty():
#The item being dequeued is taken using the head pointer
            item = self.__queue[self.__headP]
#The item's position in the queue is set to the null value "-"
            self.__queue[self.__headP] = "-"
            print(item, "has been Dequeued\n")
#If this is the last item being dequeued, then the queue will reset (Allowing more values to be added again)
            if self.__tailP == self.__headP:
                self.__tailP = -1
                self.__headP = -1
                print("Last item Dequeued: Queue Reset\n")
#Otherwise the head pointer is moved to the next item in the queue
            else:
                self.__headP += 1
            return item
        else:
            print("Queue is Empty: No items to Dequeue\n")

#Method to check if the queue is empty
    def isFull(self):
#Checks if the queue is full by seeing if the tailpointer is at the maximum index of the queue
        if self.__tailP+1 == self.__size:
            return True
        else:
            return False

#Checks if a queue is empty, by checking if the tail and head pointers are at the default
    def isEmpty(self):
        if self.__headP == -1 and self.__tailP == -1:
            return True
        else:
            return False

#Prints the Queue (USED FOR TESTING)
    def printList(self):
        print(self.__queue)

#TESTING
#Creates a new Queue
myQ = linQueue(5)
#Adds values to the queue
myQ.enqueue("Tom")
myQ.enqueue("Maddie")
myQ.enqueue("Lily")
#Deques the next item
nextInLine = myQ.dequeue()
#Adds another value to the queue
myQ.enqueue("Lucy")

#ERROR HANDLING TESTING
myQ2 = linQueue(2)
#Queue Overflow
myQ2.enqueue("Lucy")
myQ2.enqueue("Mark")
myQ2.enqueue("Andrew")
nextInLine2 = myQ2.dequeue()
myQ2.enqueue("Andrew")
#Queue Underflow
myQ2.dequeue()
myQ2.dequeue()
myQ3 = linQueue("Hello")
