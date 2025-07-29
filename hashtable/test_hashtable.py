import unittest
from hashtable import HashTable

class TestHashTable(unittest.TestCase):
    def setUp(self):
        self.hash_table = HashTable(10)  # Create a new hash table for each test

    def test_initialization(self):
        self.assertEqual(self.hash_table.total_size, 10)
        self.assertEqual(self.hash_table.current_size, 0)
        self.assertEqual(len(self.hash_table.student_list), 10)

    def test_set_and_get(self):
        # Test adding a new student
        self.hash_table.set(123, "John Doe")
        student = self.hash_table.get(123)
        self.assertIsNotNone(student)
        self.assertEqual(student.student_name, "John Doe")
        self.assertEqual(student.student_id, 123)

    def test_contains(self):
        # Test contains with non-existent student
        self.assertFalse(self.hash_table.contains(456))
        
        # Test contains with existing student
        self.hash_table.set(456, "Jane Smith")
        self.assertTrue(self.hash_table.contains(456))

    def test_remove(self):
        # Add and then remove a student
        self.hash_table.set(789, "Alice Brown")
        self.assertTrue(self.hash_table.contains(789))
        
        self.hash_table.rem(789)
        self.assertFalse(self.hash_table.contains(789))

    def test_reset(self):
        # Add some students
        self.hash_table.set(111, "Student 1")
        self.hash_table.set(222, "Student 2")
        
        # Reset the hash table
        self.hash_table.reset()
        self.assertEqual(self.hash_table.current_size, 0)
        self.assertFalse(self.hash_table.contains(111))
        self.assertFalse(self.hash_table.contains(222))

    def test_collision_handling(self):
        # Test handling of multiple students in the same slot
        # Using IDs that will hash to the same slot
        self.hash_table.set(10, "Student 10")  # Will go to slot 0
        self.hash_table.set(20, "Student 20")  # Will go to slot 0
        
        student10 = self.hash_table.get(10)
        student20 = self.hash_table.get(20)
        
        self.assertIsNotNone(student10)
        self.assertIsNotNone(student20)
        self.assertEqual(student10.student_name, "Student 10")
        self.assertEqual(student20.student_name, "Student 20")

if __name__ == '__main__':
    unittest.main()