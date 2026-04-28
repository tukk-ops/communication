class Student:
    def __init__(self, name, student_id):
       self.name = name
       self.student_id = student_id
       self.grades = {"語文":0,"數學":0,"英語":0}
    
    def set_grade(self,course,grade): 
           if course in self.grades:
            self.grades[course]= grade
    
    def print_grades(self):
        print(f"學生{self.name} (學號:{self.student_id}) 的成績為:")
        for course in self.grades:
            print(f"{course}: {self.grades[course]}分")      

chem = Student("小陳","100000")
chem.set_grade("語文",92)
chem.set_grade("數學",92)
chem.print_grades()