import json

#Data Load করলাম

def load_data():
     
    try:
        with open("student.json","r") as f:
             return json.load(f)
    except:
          return  [] # ফাইলে না থাকলে list খালি রাখবে।


# Data Save করলাম

def save_data(students):
     with open("student.json","w")as f:
          json.dump(students,f)


#Student কে add করলাম

def add_student(students):
    sid=int(input("Enter Id:"))
    
    #Duplicate check করলাম
    for s in students:
         if s["id"]==sid:
            print("ID already exists!")
            return
    name=input("Enter name:")
    age=int(input("Enter age:"))
    marks=int(input("Enter marks:"))

    student={
         "id":sid,
         "name":name,
         "age":age,
         "marks":marks
    }

    students.append(student)
    print("Student Added Successfully")

# Student কে Show করবে
#Student Existance check করবে।
def show_students(students):
     if not students:
        print("No-Students Found!")
        return
     print("\n----StudentList----")
     
     for s in students:
         print(f"ID: {s['id']} | Name: {s['name']} | Age: {s['age']} | Marks: {s['marks']}")

#Student Information Search করবো
def search_student(students):
    sid = int(input("Enter ID to search: "))

    for s in students:
        if s["id"] == sid:
            print("Student Found:")
            print(s)
            return

    print("Student not found!")

#Student Information delete করবো।
def delete_student(students):
    sid = int(input("Enter ID to delete: "))

    for s in students:
        if s["id"] == sid:
            students.remove(s)
            print("Student deleted!")
            return

    print("Student not found!")

# Student এর information Update করবে
def update_student(students):
    sid = int(input("Enter ID to update: "))

    for s in students:
        if s["id"] == sid:
            print("Leave blank if you don't want to change")

            name = input("New Name: ")
            age = input("New Age: ")
            marks = input("New Marks: ")

            if name:
                s["name"] = name
            if age:
                s["age"] = int(age)
            if marks:
                s["marks"] = int(marks)

            print("Student updated!")
            return

    print("Student not found!")

# MAIN MENU দেখাবে
def menu():
    students = load_data()

    while True:
        print("\n========= STUDENT MANAGEMENT =========")
        print("1. Add Student")
        print("2. Show All Students")
        print("3. Search Student")
        print("4. Delete Student")
        print("5. Update Student")
        print("6. Save & Exit")

        choice = input("Choose option: ")

        if choice == "1":
            add_student(students)

        elif choice == "2":
            show_students(students)

        elif choice == "3":
            search_student(students)

        elif choice == "4":
            delete_student(students)

        elif choice == "5":
            update_student(students)

        elif choice == "6":
            save_data(students)
            print("Data saved. Goodbye!")
            break

        else:
            print("Invalid choice!")

# Run করবে System Program
menu()
