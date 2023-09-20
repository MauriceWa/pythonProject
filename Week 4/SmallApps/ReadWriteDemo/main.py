def read_student():
  file = open("student_grades.txt")
  data = file.read()
  student_list = data.splitlines()
  student_dictionary_list = []

  for student in student_list:
    student_data_list = student.split(", ")
    student_dictionary = {
      "name": student_data_list[0],
      "grade": student_data_list[1]
  }
    student_dictionary_list.append(student_dictionary)
  file.close()

  return student_dictionary_list

def write_students_away(student):
  file = open("student_grades.txt", "a")
  file.write("\n" + student["name"] + ", " + student["grade"])

  file.close()
def main():

  students = read_student()
  write_students_away(students[0])

  if __name__ == "__main__":
    main()