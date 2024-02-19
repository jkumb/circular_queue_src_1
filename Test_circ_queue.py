

import unittest
from circ_queue import CircularQueue

class TestCircularQueue(unittest.TestCase):
    def test_enqueue(self):
        cq = CircularQueue(max_length=3)
        cq.enqueue(1)
        cq.enqueue(2)
        cq.enqueue(3)
        self.assertEqual(cq.queue, {0: 1, 1: 2, 2: 3})

    def test_dequeue(self):
        cq = CircularQueue(max_length=3)
        cq.enqueue(1)
        cq.enqueue(2)
        cq.enqueue(3)
        removed_element = cq.dequeue()
        print(removed_element)
        self.assertEqual(removed_element, 1)
        

    def test_full_queue(self):
        cq = CircularQueue(max_length=2)
        cq.enqueue(1)
        cq.enqueue(2)
        cq.enqueue(3)  # This should delete the oldest element (1)
        self.assertEqual(cq.queue, {1: 2, 0: 3})

    def test_empty_queue(self):
        cq = CircularQueue(max_length=3)
        removed_element = cq.dequeue()
        self.assertIsNone(removed_element)
        self.assertEqual(cq.queue, {})

if __name__ == "__main__":
    unittest.main()
