class Course:
  def __init__(self, CourseNumber = 0, CourseName = "", CourseCredit_hr = 0.0, CourseGrade = 0.0):
    CourseCredit_hr = float(CourseCredit_hr)
    CourseGrade = float(CourseGrade)
    CourseNumber = int(CourseNumber)
    if (int(CourseNumber) <  0):
      raise ValueError
    self.CourseNumber = CourseNumber
    if type(CourseName) != str:
      raise ValueError
    self.CourseName = CourseName
    if (float(CourseCredit_hr < 0)) or (float(CourseCredit_hr) > 5.0):
      raise ValueError 
    self.CourseCredit_hr = CourseCredit_hr
    if (float(CourseGrade) < 0) or (float(CourseGrade) > 4.0):
      raise ValueError
    self.CourseGrade = CourseGrade
    self.next = None

  def number(self):
    return self.CourseNumber
  
  def name(self):
    return self.CourseName

  def credit_hr(self):
    return self.CourseCredit_hr
  
  def grade(self):
    return self.CourseGrade
  
  def __str__(self):
    return (f"cs{self.CourseNumber} {self.CourseName} Grade:{self.CourseGrade} Credit Hours: {self.CourseCredit_hr}")
    
  def __iter__(self):
    pass
  
  def __next__(self):
    pass