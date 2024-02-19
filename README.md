# circular_queue_src_1
source code for circular queue implemetation

main.py:
This file demonstrates the usage of the CircularQueue class.
It reads the maximum length of the queue from an input file (input.txt).
Enqueues elements from 1 to 5 (up to the maximum length).
Demonstrates the circular behavior by adding additional elements (6 to 9).

circ_queue.py:
Contains the CircularQueue class definition.
Implements methods for enqueueing, dequeuing, and printing the queue elements.
Ensures that the queue overwrites the oldest element when it reaches its maximum length.

test_circ_queue.py:
Includes unit tests for the CircularQueue class using the unittest framework.
Tests various scenarios such as enqueueing, dequeuing, handling a full queue, and handling an empty queue.

usage:
Clone this repository to your local machine:
git clone https://github.com/your-username/circular-queue.git

Navigate to the project directory

Run the main program

Execute the unit tests
