from course import Course
class CourseList:
  def __init__(self):
    self.head = None

  def insert(self, course):
    current = self.head
    previous = None
    stop = False
    while current != None and not stop:
      if current.CourseNumber > course.CourseNumber:
        stop = True
      else:
        previous = current
        current = current.next
    temp = course
    if previous == None:
      temp.next = self.head
      self.head = temp
    else:
      temp.next = current
      previous.next = temp

  def traverse(self):
    def recurse(course):
      if course != None:
        print(course)
        recurse(course.next)
    recurse(self.head)

  def remove(self, course):
    current = self.head
    previous = None
    found = False
    while not found:
      if current.CourseNumber == course:
        found = True
      else:
        previous = current
        current = current.next
    if previous == None:
      self.head = current.next
    else:
      previous.next = current.next

  def remove_all(self, course):
    if self.head == None:
      return 'Cannot remove from an empty list'

    while self.head is not None and self.head.CourseNumber == course:
      self.head = self.head.next

    if self.head is not None:
      current = self.head
      while current.next is not None:
        if current.next.CourseNumber == course:
          current.next = current.next.next
        else:
          current = current.next

  def find(self, course):
    current = self.head
    found = False
    while current != None and not found:
      if current.CourseNumber == course:
        return current
      else:
        current = current.next
    return False
  
  def size(self):
    current = self.head
    count = 0
    while current != None:
      count += 1
      current = current.next
    return count

  def calculate_gpa(self):
    current = self.head 
    total = 0.0
    totalCredit = 0.0
    if current == None:
      return 0.0
    while current != None:
      total += current.CourseCredit_hr
      totalCredit += current.CourseCredit_hr * current.CourseGrade
      current = current.next
    return totalCredit/total

  def is_sorted(self):
    current = self.head
    prev = 0
    while current != None:
      if current.CourseNumber < prev:
        return False
      prev = current.CourseNumber
      current = current.next
    return True

  def __str__(self):
    self.first = self.head
    lyst = ""
    while self.head != None:
      lyst += f"{self.head}\n"
      self.head = self.head.next
    self.head = self.first
    return lyst

  def __iter__(self):
    self.current = None
    self.next = self.head
    return self

  def __next__(self):
    if self.next == None:
      raise StopIteration
    self.current = self.next
    self.next = self.next.next
    return self.current
    
      