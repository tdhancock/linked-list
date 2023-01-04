from course import Course
from courselist import CourseList

def main():
  cl = CourseList()
  f = open("data.txt", "r")
  lyst = f.readlines()
  i = 0
  while i < len(lyst):
    w = lyst[i].replace("\n", "")
    q = w.split(",")
    cl.insert(Course(int(q[0]), q[1], float(q[2]), float(q[3])))
    i += 1

  print(f"Current List: ({cl.size()})")
  print(cl)
  print(f"Cumulative GPA: {round(cl.calculate_gpa(),3)}")

if __name__ == "__main__":
  main()