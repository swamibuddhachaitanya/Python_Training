# Create student class which will take the name of the student as input to class,
# get the 5 subjects marks, print the total mark along with the name ,
# if the student get less than 50% mark remove the student from class ,
# finally print the total pass students


class Student:
    def __init__(self, n):
        self.name = n

    def put_marks(self, marks):
        self.marks = marks

    def print_marks_and_name(self):
        print(f"name of the student is: {self.name} \n")

        total_marks = 0
        for mark in self.marks:
            total_marks += mark

        print(f"The total marks of the student {self.name} : {total_marks} ", end="\n\n")

        return total_marks


student_list = []
student_1 = Student("Harish")
student_1.put_marks([10, 20, 30, 40, 50])
student_list.append(student_1)

student_2 = Student("Naman")
student_2.put_marks([20, 20, 40, 40, 70])
student_list.append(student_2)
full_marks = 500

for s in student_list:
    total_marks = s.print_marks_and_name()
    if (total_marks/full_marks) < 0.5:
        print(f"student : {s.name} has failed" )
        del(s)

