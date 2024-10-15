from lib.student import Student

def test_student_constructs():
    student = Student("Kelly Howes", "Sept 2024 foundations ra")
    assert student.full_name == "Kelly Howes"
    assert student.cohort == "Sept 2024 foundations ra"

def test_students_format_nicely():
    student = Student("Kelly Howes", "Sept 2024 foundations ra")
    assert str(student) == "Name:Kelly Howes,Cohort:Sept 2024 foundations ra"