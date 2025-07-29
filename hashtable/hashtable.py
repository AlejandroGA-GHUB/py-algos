# my version

class HashTable:
    #
    class StudentData:
        def __init__(self, student_id, student_name):
            self.student_id = student_id
            self.student_name = student_name
            self.status = True

    #
    def __init__(self, total_size):
        self.total_size = total_size
        self.student_list = []
        self.current_size = 0

        for i in range(total_size):
            self.student_list.append([])

    #
    def size(self):
        return self.current_size
    
    #
    def contains(self, student_id):

        slot = self.get_slot(student_id)

        for entry in slot:
            if entry.status and entry.student_id == student_id:
                return True
        
        return False

    #
    def get_slot(self, student_id):
        return self.student_list[student_id % self.total_size]
    
    #
    def reset(self):

        for slot in self.student_list:
            slot.clear()
        
        self.current_size = 0
   
    #
    def set(self, student_id, student_name):

        currentEntry = self.get(student_id)
        if currentEntry != None:
            currentEntry.student_name = student_name
            return

        slot = self.get_slot(student_id)
        empty_entry = self.search_for_empty_entry(slot)

        if empty_entry != None:
            empty_entry.student_id = student_id
            empty_entry.student_name = student_name
            empty_entry.status = True
            self.current_size += 1
            return
        
        student = self.StudentData(student_id, student_name)

        slot.append(student)
        self.current_size += 1

    #
    def rem(self, student_id):

        slot = self.get_slot(student_id)

        for entry in slot:
            if entry.student_id == student_id:
                entry.status = False
                self.current_size -= 1
                break
    
    #
    def search_for_empty_entry(self, slot):

        for entry in slot:
            if entry.status == False:
                return entry

        return None
    
    #
    def get(self, student_id):

        slot = self.get_slot(student_id)

        for entry in slot:
            if entry.status != False and entry.student_id == student_id:
                return entry
        
        return None

#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
# co-pilot version

class HashTable:
    class StudentData:
        """Inner class representing a student record"""
        def __init__(self, student_id: int, student_name: str):
            self.student_id = student_id
            self.student_name = student_name
            self.status = True

    def __init__(self, total_size: int):
        """Initialize hash table with specified size"""
        self.total_size = total_size
        self.student_list = [[] for _ in range(total_size)]
        self.current_size = 0

    def size(self) -> int:
        """Return current number of active entries"""
        return self.current_size
    
    def contains(self, student_id: int) -> bool:
        """Check if student exists and is active in hash table"""
        slot = self.get_slot(student_id)
        return any(
            entry.status and entry.student_id == student_id 
            for entry in slot
        )

    def get_slot(self, student_id: int) -> list:
        """Get the appropriate slot for a student ID"""
        return self.student_list[student_id % self.total_size]
    
    def reset(self) -> None:
        """Clear all entries from the hash table"""
        for slot in self.student_list:
            slot.clear()
        self.current_size = 0
    
    def set(self, student_id: int, student_name: str) -> None:
        """Add or update a student entry"""
        # Check if student exists
        current_entry = self.get(student_id)
        if current_entry:
            current_entry.student_name = student_name
            return

        # Try to find empty slot
        slot = self.get_slot(student_id)
        empty_entry = self.search_for_empty_entry(slot)

        if empty_entry:
            empty_entry.student_id = student_id
            empty_entry.student_name = student_name
            empty_entry.status = True
        else:
            # Create new entry if no empty slot found
            student = self.StudentData(student_id, student_name)
            slot.append(student)
            
        self.current_size += 1

    def rem(self, student_id: int) -> None:
        """Mark a student entry as inactive"""
        slot = self.get_slot(student_id)
        for entry in slot:
            if entry.student_id == student_id:
                entry.status = False
                self.current_size -= 1
                break
    
    def search_for_empty_entry(self, slot: list) -> StudentData:
        """Find first inactive entry in a slot"""
        for entry in slot:
            if not entry.status:
                return entry
        return None
    
    def get(self, student_id: int) -> StudentData:
        """Retrieve active student entry by ID"""
        slot = self.get_slot(student_id)
        for entry in slot:
            if entry.status and entry.student_id == student_id:
                return entry
        return None