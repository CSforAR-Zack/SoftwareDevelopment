import unittest
from data_structs_lib import Stack, Queue


class TestStack(unittest.TestCase):
    """Tests for the Stack Class (Last-In, First-Out)"""

    def setUp(self):
        """This runs before EVERY test function to ensure a fresh Stack."""
        self.stack = Stack()

    def test_is_empty_on_new(self):
        """Test that a new stack is considered empty."""
        self.assertTrue(self.stack.is_empty())

    def test_push_and_pop_logic(self):
        """Test the LIFO (Last-In, First-Out) behavior."""
        # Push items
        self.stack.enter_value(1)
        self.stack.enter_value(2)
        self.stack.enter_value(3)

        # Pop items (Should come out in reverse order: 3, 2, 1)
        self.assertEqual(self.stack.get_value(), 3)
        self.assertEqual(self.stack.get_value(), 2)
        self.assertEqual(self.stack.get_value(), 1)

    def test_peek_does_not_remove(self):
        """Test that viewing the next item does not remove it."""
        self.stack.enter_value(100)
        
        # View it
        seen_item = self.stack.view_next()
        self.assertEqual(seen_item, 100)
        
        # Ensure it is still there (stack is not empty)
        self.assertFalse(self.stack.is_empty())
        
        # Ensure we can still pop it
        self.assertEqual(self.stack.get_value(), 100)

    def test_pop_empty_returns_none(self):
        """Test that popping an empty stack returns None (avoids crash)."""
        result = self.stack.get_value()
        self.assertIsNone(result)


class TestQueue(unittest.TestCase):
    """Tests for the Queue Class (First-In, First-Out)"""

    def setUp(self):
        """This runs before EVERY test function to ensure a fresh Queue."""
        self.queue = Queue()

    def test_is_empty_on_new(self):
        """Test that a new queue is considered empty."""
        self.assertTrue(self.queue.is_empty())

    def test_add_and_remove_logic(self):
        """Test the FIFO (First-In, First-Out) behavior."""
        # Add items
        self.queue.enter_value("First")
        self.queue.enter_value("Second")
        self.queue.enter_value("Third")

        # Remove items (Should come out in original order)
        self.assertEqual(self.queue.get_value(), "First")
        self.assertEqual(self.queue.get_value(), "Second")
        self.assertEqual(self.queue.get_value(), "Third")

    def test_peek_does_not_remove(self):
        """Test that viewing the next item does not remove it."""
        self.queue.enter_value(50)
        
        # View it
        seen_item = self.queue.view_next()
        self.assertEqual(seen_item, 50)
        
        # Ensure it is still there
        self.assertFalse(self.queue.is_empty())

    def test_remove_empty_returns_none(self):
        """Test that removing from an empty queue returns None."""
        result = self.queue.get_value()
        self.assertIsNone(result)

if __name__ == '__main__':
    unittest.main()