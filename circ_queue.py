'''
Initializes a circular queue with the specified maximum length.
enqueue:Add an element to the circular queue.
de queue: Removes the latest element from the circular queue.
print queue:Prints the elements in the circular queue.
       
       '''
class CircularQueue:
    def __init__(self, max_length):
        self.max_length = max_length
        self.queue = {}
        self.front = self.rear = -1

    def enqueue(self, data):
        if (self.rear + 1) % self.max_length == self.front:
            print("The circular queue is full. Deleting the latest element.")
            self.dequeue()

        if self.front == -1:
            self.front = self.rear = 0
        else:
            self.rear = (self.rear + 1) % self.max_length

        self.queue[self.rear] = data

    def dequeue(self):
        if self.front == -1:
            print("The circular queue is empty.")
            return None

        removed_element = self.queue[self.front]
        if self.front == self.rear:
            self.front = self.rear = -1
        else:
            self.front = (self.front + 1) % self.max_length

        return removed_element

    def print_queue(self):
        if self.front == -1:
            print("No element in the circular queue.")
        elif self.rear >= self.front:
            for i in range(self.front, self.rear + 1):
                print(self.queue[i], end=" ")
        else:
            for i in range(self.front, self.max_length):
                print(self.queue[i], end=" ")
            for i in range(0, self.rear + 1):
                print(self.queue[i], end=" ")
        print()
