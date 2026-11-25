from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field


app = FastAPI(title="FastAPI Practice App")


class Student(BaseModel):
    name: str = Field(min_length=2)
    age: int = Field(gt=0, le=120)
    course: str
    score: float = Field(ge=0, le=100)


students: dict[int, Student] = {
    1: Student(name="Anu", age=22, course="Python", score=87.5),
    2: Student(name="Ravi", age=24, course="FastAPI", score=91.0),
}


@app.get("/")
def home():
    return {"message": "Welcome to FastAPI practice"}


@app.get("/hello/{name}")
def say_hello(name: str):
    return {"message": f"Hello, {name}"}


@app.get("/add")
def add_numbers(a: int, b: int):
    return {"a": a, "b": b, "sum": a + b}


@app.get("/students")
def get_students():
    return students


@app.get("/students/{student_id}")
def get_student(student_id: int):
    if student_id not in students:
        raise HTTPException(status_code=404, detail="Student not found")
    return students[student_id]


@app.post("/students")
def create_student(student: Student):
    new_id = max(students) + 1 if students else 1
    students[new_id] = student
    return {"id": new_id, "student": student}


@app.put("/students/{student_id}")
def update_student(student_id: int, student: Student):
    if student_id not in students:
        raise HTTPException(status_code=404, detail="Student not found")
    students[student_id] = student
    return {"id": student_id, "student": student}


@app.delete("/students/{student_id}")
def delete_student(student_id: int):
    if student_id not in students:
        raise HTTPException(status_code=404, detail="Student not found")
    deleted_student = students.pop(student_id)
    return {"message": "Student deleted", "student": deleted_student}


@app.get("/students/search/")
def search_students(course: str | None = None, minimum_score: float = 0):
    result = []

    for student_id, student in students.items():
        course_matches = course is None or student.course.lower() == course.lower()
        score_matches = student.score >= minimum_score

        if course_matches and score_matches:
            result.append({"id": student_id, "student": student})

    return result
