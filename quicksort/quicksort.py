# implement quicksort
# pass a comparator to the quick_sort(), could be ascending or descending

# we have a student class, say height and weight
# comparator in quick_sort() is taking in 2 objects (height and weight for visual here, but could be anything)
# callback could be used here

# Client code student class example
class Student:
    def __init__(self, name, height, weight):
        self.name = name
        self.height = height  # in cm
        self.weight = weight  # in kg
    
    def __repr__(self):
        return f"Student({self.name}, h:{self.height}cm, w:{self.weight}kg)"

def quick_sort(arr, comparator):
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
    right = []
    
    for item in arr:

        if item == pivot:
            continue

        comparison_result = comparator(item, pivot)
        
        if comparison_result:  
            left.append(item)
        else:  
            right.append(item)
    
    return quick_sort(left, comparator) + [pivot] + quick_sort(right, comparator)

# COMPARATOR FUNCTIONS - Extract/compare values from complete Student objects
def height_comparator_ascending(student1, student2):
    """Compare students by height - receives full Student objects"""
    return student1.height < student2.height

def weight_comparator_ascending(student1, student2):
    """Compare students by weight - receives full Student objects"""
    return student1.weight < student2.weight

def height_comparator_descending(student1, student2):
    """Compare students by height - receives full Student objects"""
    return student1.height >= student2.height

def weight_comparator_descending(student1, student2):
    """Compare students by weight - receives full Student objects"""
    return student1.weight >= student2.weight

def name_comparator_ascending(student1, student2):
    """Compare students by name alphabetically - receives full Student objects"""
    return student1.name < student2.name
    
def name_comparator_descending(student1, student2):
    """Compare students by name alphabetically - receives full Student objects"""
    return student1.name >= student2.name

def bmi_comparator_ascending(student1, student2):
    """Compare students by BMI (weight/height²) - receives full Student objects"""
    # BMI = weight(kg) / height(m)²
    bmi1 = student1.weight / ((student1.height/100) ** 2)
    bmi2 = student2.weight / ((student2.height/100) ** 2)
    return bmi1 < bmi2

def composite_comparator_ascending(student1, student2):
    """Compare by height first, then by weight if heights are equal"""
    if student1.height != student2.height:
        return student1.height < student2.height
    else:
        return student1.weight < student2.weight  # Tie-breaker


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
    result1 = quick_sort(students, height_comparator_ascending)
    for student in result1:
        print(f"  {student}")
    print()
    
    # Example 2: Sort by height (descending) - same comparator, different callback
    print("=== Height Descending ===")
    result2 = quick_sort(students, height_comparator_descending)
    for student in result2:
        print(f"  {student}")
    print()
    
    # Example 3: Sort by weight (ascending) - different comparator, same callback
    print("=== Weight Ascending ===")
    result3 = quick_sort(students, weight_comparator_ascending)
    for student in result3:
        print(f"  {student}")
    print()
    
    # Example 4: Sort by name (alphabetical)
    print("=== Name Alphabetical ===")
    result4 = quick_sort(students, name_comparator_ascending)
    for student in result4:
        print(f"  {student}")
    print()
    
    # Example 5: Sort by BMI (Body Mass Index)
    print("=== BMI Ascending ===")
    result5 = quick_sort(students, bmi_comparator_ascending)
    for student in result5:
        bmi = student.weight / ((student.height/100) ** 2)
        print(f"  {student} (BMI: {bmi:.1f})")
    print()
    
    # Example 6: Composite sorting (height first, then weight)
    print("=== Height then Weight (Ascending) ===")
    result6 = quick_sort(students, composite_comparator_ascending)
    for student in result6:
        print(f"  {student}")
    print()
    
    print("Key Points:")
    print("- Each comparator receives COMPLETE Student objects")
    print("- Comparators can access any property (height, weight, name)")
    print("- Comparators return boolean values for direct comparison")
    print("- Different comparators handle different sorting criteria")
    print("- Ascending/descending logic is built into each comparator")