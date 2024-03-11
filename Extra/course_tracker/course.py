import tkinter as tk
from tkinter import ttk
import json
from uuid import uuid4

data_filename = 'course_data.json'

def save_course(edit=False, course_id_to_edit=None):
    try:
        course_name = course_entry.get().strip()
        total_lessons = (total_entry.get()).strip()
        completed_lessons = (completed_entry.get()).strip()

        if not total_lessons.isdigit() or not completed_lessons.isdigit():
            raise ValueError("Total lessons and completed lessons must be numeric.")

        total_lessons_final = int(total_lessons)
        completed_lessons_final = int(completed_lessons)

        if edit:
            course_id = course_id_to_edit
        else:
            course_id = str(uuid4())

        new_course = {
            "id": course_id,
            "name": course_name,
            "total_lessons": total_lessons_final,
            "completed_lessons": completed_lessons_final
        }

        try:
            with open(data_filename, 'r') as file:
                data = json.load(file)
        except FileNotFoundError:
            data = {"courses": []}

        if edit:
            for i, course in enumerate(data["courses"]):
                if course["id"] == course_id:
                    data["courses"][i] = new_course
                    break
        else:
            data["courses"].append(new_course)

        with open(data_filename, 'w') as file:
            json.dump(data, file, indent=4)

        if edit:
            progress_label.config(text=f"Course updated with ID: {course_id}")
        else:
            progress_label.config(text=f"Course saved with ID: {course_id}")
        refresh_courses()

    except ValueError as e:
        progress_label.config(text=str(e))

def load_courses():
    try:
        with open(data_filename, 'r') as file:
            data = json.load(file)
            return data.get("courses", [])
    except (FileNotFoundError, json.JSONDecodeError):
        with open(data_filename, 'w') as file:
            json.dump({"courses": []}, file, indent=4)
        return []

def populate_courses_on_startup():
    refresh_courses()

def refresh_courses():
    courses = load_courses()
    courses_listbox.delete(0, tk.END)
    for course in courses:
        if course["total_lessons"] > 0:
            completion_percentage = (course["completed_lessons"] / course["total_lessons"]) * 100
        else:
            completion_percentage = 0
        courses_listbox.insert(tk.END,
                               f'{course["name"]} - {course["completed_lessons"]}/{course["total_lessons"]} '
                               f'({completion_percentage:.2f}%) ({course["id"]})')

def edit_course():
    selected = courses_listbox.curselection()
    if not selected:
        progress_label.config(text="Please select a course to edit")
        return
    else:
        selected_index = selected[0]
        course_info = courses_listbox.get(selected_index)
        course_id = course_info.split('(')[-1].rstrip(')')

        courses = load_courses()
        for course in courses:
            if course["id"] == course_id:
                course_entry.delete(0, tk.END)
                course_entry.insert(0, course["name"])
                total_entry.delete(0, tk.END)
                total_entry.insert(0, str(course["total_lessons"]))
                completed_entry.delete(0, tk.END)
                completed_entry.insert(0, str(course["completed_lessons"]))
                save_button.config(command=lambda: save_course(edit=True, course_id_to_edit=course_id))
                break

app = tk.Tk()
app.title("Course Progress Tracker")

frame = ttk.Frame(app)
frame.pack(padx=10, pady=10, expand=True, fill=tk.BOTH)

courses_listbox = tk.Listbox(frame, width=50, height=10)
courses_listbox.grid(column=0, row=0, columnspan=2, pady=5)

refresh_button = ttk.Button(frame, text="Refresh Courses", command=refresh_courses)
refresh_button.grid(column=0, row=1, columnspan=2)

edit_button = ttk.Button(frame, text="Edit Selected Course", command=edit_course)
edit_button.grid(column=0, row=2, columnspan=2)

ttk.Label(frame, text="Course Name:").grid(column=0, row=3, sticky=tk.W)
course_entry = ttk.Entry(frame, width=20)
course_entry.grid(column=1, row=3, sticky=tk.W)

ttk.Label(frame, text="Total Lessons:").grid(column=0, row=4, sticky=tk.W)
total_entry = ttk.Entry(frame, width=20)
total_entry.grid(column=1, row=4, sticky=tk.W)

ttk.Label(frame, text="Completed Lessons:").grid(column=0, row=5, sticky=tk.W)
completed_entry = ttk.Entry(frame, width=20)
completed_entry.grid(column=1, row=5, sticky=tk.W)

save_button = ttk.Button(frame, text="Save Course", command=lambda: save_course(edit=False))
save_button.grid(column=1, row=6, sticky=tk.W, pady=5)

progress_label = ttk.Label(frame, text="Welcome to Course Tracker")
progress_label.grid(column=0, row=7, columnspan=2, sticky=tk.W)

populate_courses_on_startup()

app.mainloop()
