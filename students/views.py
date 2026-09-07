from django.shortcuts import render, get_object_or_404

from .models import Student, Course, Department


def home(request):
    students_count = Student.objects.count()
    courses_count = Course.objects.count()
    departments_count = Department.objects.count()

    return render(
        request,
        'home.html',
        {
            'students_count': students_count,
            'courses_count': courses_count,
            'departments_count': departments_count,
        }
    )


def students(request):
    all_students = Student.objects.all()

    return render(
        request,
        'students.html',
        {
            'students': all_students,
        }
    )


def student_detail(request, student_id):
    student = get_object_or_404(Student, id=student_id)

    return render(
        request,
        'student_detail.html',
        {
            'student': student,
        }
    )


def courses(request):
    all_courses = Course.objects.all()

    return render(
        request,
        'courses.html',
        {
            'courses': all_courses,
        }
    )


def course_detail(request, course_id):
    course = get_object_or_404(Course, id=course_id)

    return render(
        request,
        'course_detail.html',
        {
            'course': course,
        }
    )


def departments(request):
    all_departments = Department.objects.all()

    return render(
        request,
        'departments.html',
        {
            'departments': all_departments,
        }
    )