'''
Import the CircularQueue class from the circ_queue module
Get the current working directory
Construct the file path to read the input from 'input.txt'
Read the maximum length from the input file
Create an instance of the CircularQueue with the specified maximum length
Enqueue elements from 1 to 5 (up to the maximum length)
Enqueue additional elements from 6 to 9 (overwriting the oldest elements if needed)
'''
import os
from circ_queue import CircularQueue

cwd = os.getcwd()
file_path=os.path.join(cwd,'input','input.txt')
f=open(file_path,'r')
max_length = int(f.read())

cq = CircularQueue(max_length)

for i in range(1,6):
    if i<=max_length:
        cq.enqueue(i)       
    
print("Initial queue:")
cq.print_queue()

for j in range(6,10):
    print()
    cq.enqueue(j)  # This will delete the latest element 
    print("After adding j:")
    cq.print_queue()

