import pytest
from hashtable import HashTable

@pytest.fixture
def hash_table():
    return HashTable(10)

def test_initialization(hash_table):
    assert hash_table.total_size == 10
    assert hash_table.current_size == 0
    assert len(hash_table.student_list) == 10

def test_set_and_get(hash_table):
    hash_table.set(123, "John Doe")
    student = hash_table.get(123)
    assert student is not None
    assert student.student_name == "John Doe"
    assert student.student_id == 123

def test_contains(hash_table):
    assert not hash_table.contains(456)
    hash_table.set(456, "Jane Smith")
    assert hash_table.contains(456)

def test_remove(hash_table):
    hash_table.set(789, "Alice Brown")
    assert hash_table.contains(789)
    hash_table.rem(789)
    assert not hash_table.contains(789)

def test_reset(hash_table):
    hash_table.set(111, "Student 1")
    hash_table.set(222, "Student 2")
    hash_table.reset()
    assert hash_table.current_size == 0
    assert not hash_table.contains(111)
    assert not hash_table.contains(222)

def test_collision_handling(hash_table):
    hash_table.set(10, "Student 10")  # slot 0
    hash_table.set(20, "Student 20")  # slot 0
    student10 = hash_table.get(10)
    student20 = hash_table.get(20)
    assert student10 is not None
    assert student20 is not None
    assert student10.student_name == "Student 10"
    assert student20.student_name == "Student 20"
