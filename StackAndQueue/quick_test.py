# Quick test for Stack functionality
import unittest
from data_structs_lib import Stack


class TestStack(unittest.TestCase):

    def test_stack_behavior(self):
        # 1. ARRANGE: Create the stack
        my_stack = Stack()
        
        # 2. ACT: Add items (Push)
        my_stack.enter_value(10)
        my_stack.enter_value(20)

        # 3. ASSERT: Remove items (Pop) and check logic
        # Expect 20 first because Stack is "Last-In, First-Out"
        self.assertEqual(my_stack.get_value(), 20) 
        self.assertEqual(my_stack.get_value(), 10)

    def test_empty_stack(self):
        # Test that a new stack is actually empty
        my_stack = Stack()
        self.assertTrue(my_stack.is_empty())


if __name__ == '__main__':
    unittest.main()