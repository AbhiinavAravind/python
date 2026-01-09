frontend_students = {"Anu", "Rahul", "Meera", "Kiran"}
backend_students = {"Rahul", "Vishnu", "Meera", "Suresh"}


backend_students.add("Neha")


frontend_students.remove("Kiran")


both_courses = frontend_students & backend_students


backend_only = backend_students - frontend_students

total_unique_students = frontend_students | backend_students


course_counts = {
    "Frontend": len(frontend_students),
    "Backend": len(backend_students)
}


for course, count in course_counts.items():
    print(f"{course} course has {count} students")


updated_courses = {
    course: count for course, count in course_counts.items()
}
updated_courses["Fullstack"] = course_counts["Frontend"] + course_counts["Backend"]


print( frontend_students)
print( backend_students)
print( both_courses)
print( backend_only)
print( len(total_unique_students))
print( updated_courses)