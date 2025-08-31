# implement quicksort
# pass a comparator to the quick_sort(), could be ascending or descending

# we have a student class, say height and weight
# comparator in quick_sort() is taking in 2 objects (height and weight for visual here, but could be anything)
# callback could be used here

class Student:
    def __init__(self, name, height, weight):
        self.name = name
        self.height = height  # in cm
        self.weight = weight  # in kg
    
    def __repr__(self):
        return f"Student({self.name}, h:{self.height}cm, w:{self.weight}kg)"

def quick_sort(arr, comparator, ordering_callback):
    """
    QuickSort with separate comparator and ordering logic
    
    Args:
        arr: List of objects to sort
        comparator: Function that extracts/compares values from two objects
                   Takes two complete objects, returns comparison result
        ordering_callback: Function that takes comparison result and decides ordering
                          Returns True if first should come before second
    """
    if len(arr) <= 1:
        return arr
    
    pivot = arr[len(arr) // 2]
    
    left = []
    middle = []
    right = []
    
    for item in arr:
        comparison_result = comparator(item, pivot)
        
        if comparison_result == 0:  # Equal
            middle.append(item)
        elif ordering_callback(comparison_result):  # Should come before pivot
            left.append(item)
        else:  # Should come after pivot
            right.append(item)
    
    return quick_sort(left, comparator, ordering_callback) + middle + quick_sort(right, comparator, ordering_callback)

# COMPARATOR FUNCTIONS - Extract/compare values from complete Student objects
def height_comparator(student1, student2):
    """Compare students by height - receives full Student objects"""
    return student1.height - student2.height

def weight_comparator(student1, student2):
    """Compare students by weight - receives full Student objects"""
    return student1.weight - student2.weight

def name_comparator(student1, student2):
    """Compare students by name alphabetically - receives full Student objects"""
    if student1.name < student2.name:
        return -1
    elif student1.name > student2.name:
        return 1
    else:
        return 0

def bmi_comparator(student1, student2):
    """Compare students by BMI (weight/height²) - receives full Student objects"""
    # BMI = weight(kg) / height(m)²
    bmi1 = student1.weight / ((student1.height/100) ** 2)
    bmi2 = student2.weight / ((student2.height/100) ** 2)
    return bmi1 - bmi2

def composite_comparator(student1, student2):
    """Compare by height first, then by weight if heights are equal"""
    height_diff = student1.height - student2.height
    if height_diff != 0:
        return height_diff
    else:
        return student1.weight - student2.weight  # Tie-breaker

# ORDERING CALLBACKS - Decide direction based on comparison result
def ascending_order(comparison_result):
    """True if first item should come before second (ascending order)"""
    return comparison_result < 0

def descending_order(comparison_result):
    """True if first item should come before second (descending order)"""
    return comparison_result > 0

# EXAMPLE USAGE AND TESTING
if __name__ == "__main__":
    # Create sample data - each student has ALL their information
    students = [
        Student("Alice", 165, 55),
        Student("Bob", 180, 75),
        Student("Charlie", 170, 65),
        Student("Diana", 160, 50),
        Student("Eve", 175, 60),
        Student("Frank", 185, 80)
    ]
    
    print("Original students:")
    for student in students:
        print(f"  {student}")
    print()
    
    # Example 1: Sort by height (ascending)
    print("=== Height Ascending ===")
    result1 = quick_sort(students, height_comparator, ascending_order)
    for student in result1:
        print(f"  {student}")
    print()
    
    # Example 2: Sort by height (descending) - same comparator, different callback
    print("=== Height Descending ===")
    result2 = quick_sort(students, height_comparator, descending_order)
    for student in result2:
        print(f"  {student}")
    print()
    
    # Example 3: Sort by weight (ascending) - different comparator, same callback
    print("=== Weight Ascending ===")
    result3 = quick_sort(students, weight_comparator, ascending_order)
    for student in result3:
        print(f"  {student}")
    print()
    
    # Example 4: Sort by name (alphabetical)
    print("=== Name Alphabetical ===")
    result4 = quick_sort(students, name_comparator, ascending_order)
    for student in result4:
        print(f"  {student}")
    print()
    
    # Example 5: Sort by BMI (Body Mass Index)
    print("=== BMI Ascending ===")
    result5 = quick_sort(students, bmi_comparator, ascending_order)
    for student in result5:
        bmi = student.weight / ((student.height/100) ** 2)
        print(f"  {student} (BMI: {bmi:.1f})")
    print()
    
    # Example 6: Composite sorting (height first, then weight)
    print("=== Height then Weight (Ascending) ===")
    result6 = quick_sort(students, composite_comparator, ascending_order)
    for student in result6:
        print(f"  {student}")
    print()
    
    print("Key Points:")
    print("- Each comparator receives COMPLETE Student objects")
    print("- Comparators can access any property (height, weight, name)")
    print("- Ordering callbacks determine ascending/descending direction")
    print("- Same comparator works with different ordering callbacks")
    print("- Same ordering callback works with different comparators")