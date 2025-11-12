# student_management.py
# Perfect example for students to understand Classes and Objects!
# This is like a mini school management system

class Student:
    """
    Blueprint for creating student records
    Just like a school form that every student fills
    """
    
    # Class variable - same for all students
    school_name = "Delhi Public School"
    total_students = 0
    
    def __init__(self, roll_no, name, standard, marks_math, marks_science, marks_english):
        """
        Constructor - called when creating a new student
        Like filling a new admission form
        """
        # Instance variables - unique for each student
        self.roll_no = roll_no
        self.name = name
        self.standard = standard
        self.marks_math = marks_math
        self.marks_science = marks_science
        self.marks_english = marks_english
        
        # Increment total students count
        Student.total_students += 1
    
    def calculate_total(self):
        """Each student can calculate their own total marks"""
        return self.marks_math + self.marks_science + self.marks_english
    
    def calculate_percentage(self):
        """Each student can calculate their own percentage"""
        total = self.calculate_total()
        return (total / 300) * 100
    
    def get_grade(self):
        """Each student can get their grade based on percentage"""
        percentage = self.calculate_percentage()
        
        if percentage >= 90:
            return "A+ (Outstanding)"
        elif percentage >= 80:
            return "A (Excellent)"
        elif percentage >= 70:
            return "B (Good)"
        elif percentage >= 60:
            return "C (Average)"
        elif percentage >= 50:
            return "D (Pass)"
        else:
            return "F (Need Improvement)"
    
    def print_report_card(self):
        """Each student can print their own report card"""
        print(f"\n{'='*50}")
        print(f"🏫 {Student.school_name}")
        print(f"📄 REPORT CARD")
        print(f"{'='*50}")
        print(f"Roll No: {self.roll_no}")
        print(f"Name: {self.name}")
        print(f"Standard: {self.standard}")
        print(f"-" * 50)
        print(f"📚 MARKS:")
        print(f"  Mathematics    : {self.marks_math}/100")
        print(f"  Science        : {self.marks_science}/100")
        print(f"  English        : {self.marks_english}/100")
        print(f"-" * 50)
        print(f"📊 PERFORMANCE:")
        print(f"  Total Marks    : {self.calculate_total()}/300")
        print(f"  Percentage     : {self.calculate_percentage():.2f}%")
        print(f"  Grade          : {self.get_grade()}")
        print(f"{'='*50}")
    
    def needs_improvement_in(self):
        """Check which subjects need improvement (marks < 60)"""
        weak_subjects = []
        
        if self.marks_math < 60:
            weak_subjects.append("Mathematics")
        if self.marks_science < 60:
            weak_subjects.append("Science")
        if self.marks_english < 60:
            weak_subjects.append("English")
        
        return weak_subjects
    
    @classmethod
    def print_school_stats(cls):
        """Print statistics for the entire school"""
        print(f"\n{'='*50}")
        print(f"🏫 {cls.school_name} - Statistics")
        print(f"{'='*50}")
        print(f"Total Students: {cls.total_students}")
        print(f"{'='*50}")


# ============================================================
# Creating student OBJECTS - each one is a real student!
# ============================================================

print("🎓 STUDENT MANAGEMENT SYSTEM")
print("="*60)
print("Creating student records using the Student class...")
print()

# Create students - Notice how easy it is!
student1 = Student(101, "Rahul Sharma", "10th", 95, 88, 92)
student2 = Student(102, "Ananya Patel", "10th", 78, 85, 80)
student3 = Student(103, "Vikram Singh", "10th", 92, 95, 89)
student4 = Student(104, "Priya Reddy", "10th", 56, 62, 58)
student5 = Student(105, "Arjun Verma", "10th", 88, 90, 85)

print("✅ 5 students created successfully!")

# ============================================================
# Each student can perform actions by themselves!
# ============================================================

# Print report cards for all students
print("\n" + "="*60)
print("📋 GENERATING REPORT CARDS")
print("="*60)

student1.print_report_card()
student2.print_report_card()
student3.print_report_card()
student4.print_report_card()
student5.print_report_card()

# ============================================================
# Find class topper
# ============================================================

print("\n" + "="*60)
print("🏆 FINDING CLASS TOPPER")
print("="*60)

students = [student1, student2, student3, student4, student5]
topper = max(students, key=lambda s: s.calculate_total())

print(f"\n🎉 Class Topper: {topper.name}")
print(f"   Roll No: {topper.roll_no}")
print(f"   Total Marks: {topper.calculate_total()}/300")
print(f"   Percentage: {topper.calculate_percentage():.2f}%")
print(f"   Grade: {topper.get_grade()}")

# ============================================================
# Find students who need improvement
# ============================================================

print("\n" + "="*60)
print("📌 STUDENTS NEEDING EXTRA ATTENTION")
print("="*60)

for student in students:
    weak_subjects = student.needs_improvement_in()
    if weak_subjects:
        print(f"\n👤 {student.name} (Roll: {student.roll_no})")
        print(f"   Needs improvement in: {', '.join(weak_subjects)}")
        print(f"   Current Percentage: {student.calculate_percentage():.2f}%")

# ============================================================
# Calculate class average
# ============================================================

print("\n" + "="*60)
print("📊 CLASS STATISTICS")
print("="*60)

total_percentage = sum(s.calculate_percentage() for s in students)
class_average = total_percentage / len(students)

print(f"\nClass Average: {class_average:.2f}%")
print(f"Highest Score: {topper.calculate_percentage():.2f}% ({topper.name})")

lowest_scorer = min(students, key=lambda s: s.calculate_total())
print(f"Lowest Score: {lowest_scorer.calculate_percentage():.2f}% ({lowest_scorer.name})")

# Print school statistics
Student.print_school_stats()

# ============================================================
# The Magic of Classes and Objects!
# ============================================================

print("\n" + "="*60)
print("✨ THE MAGIC OF CLASSES AND OBJECTS!")
print("="*60)
print("\n✅ What we did:")
print("   • Defined Student class ONCE")
print("   • Created 5 different students easily")
print("   • Each student manages their own data")
print("   • Each student can perform actions (calculate, print)")
print("   • Added new students? Just one line each!")
print("   • Want to add 'attendance' field? Add once in class!")
print("\n❌ Without classes, we would need:")
print("   • 30+ variables (6 per student)")
print("   • Repeat calculation logic 5 times")
print("   • Repeat printing logic 5 times")
print("   • Nightmare to maintain!")
print("\n🎯 This is why every modern software uses OOP!")
print("="*60)