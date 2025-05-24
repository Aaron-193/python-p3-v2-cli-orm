from models.department import Department
from models.employee import Employee

def exit_program():
    print("Goodbye!")
    exit()

# Department Functions
def list_departments():
    departments = Department.get_all()
    for department in departments:
        print(department)

def find_department_by_name():
    name = input("Enter the department's name: ")
    department = Department.find_by_name(name)
    print(department) if department else print(f'Department {name} not found')

def find_department_by_id():
    id_ = input("Enter the department's ID: ")  # Changed 'id' to 'id_' to avoid overriding built-in 'id'
    department = Department.find_by_id(id_)
    print(department) if department else print(f"Department {id_} not found")

def create_department():
    name = input("Enter the department's name: ")
    location = input("Enter the department's location: ")
    try:
        department = Department.create(name, location)
        print(f'Success: {department}')
    except Exception as exc:
        print("Error creating department: ", exc)

def update_department():
    id_ = input("Enter the department's ID: ")
    department = Department.find_by_id(id_)

    if department:
        try:
            name = input("Enter the department's new name: ")
            department.name = name
            location = input("Enter the department's new location: ")
            department.location = location

            department.update()
            print(f"Success: {department}")  # Fixed string formatting
        except Exception as exc:
            print("Error updating department: ", exc)
    else:
        print(f'Department {id_} not found')

def delete_department():
    id_ = input("Enter the department's ID: ")
    department = Department.find_by_id(id_)
    if department:
        department.delete()
        print(f"Department {id_} deleted")
    else:
        print(f'Department {id_} not found')

# Employee Functions
def list_employees():
    employees = Employee.get_all()
    for employee in employees:
        print(employee)

def find_employee_by_name():
    name = input("Enter the employee's name: ")
    employee = Employee.find_by_name(name)
    print(employee) if employee else print(f"Employee {name} not found")

def find_employee_by_id():
    id_ = input("Enter the employee's ID: ")
    employee = Employee.find_by_id(id_)
    print(employee) if employee else print(f"Employee {id_} not found")

def create_employee():
    name = input("Enter the employee's name: ")
    job_title = input("Enter the employee's job title: ")
    department_id = input("Enter the employee's department ID: ")
    try:
        employee = Employee.create(name, job_title, department_id)
        print(f'Success: {employee}')  # Added success message
    except Exception as exc:
        print("Error creating employee: ", exc)

def update_employee():
    id_ = input("Enter the employee's ID: ")
    employee = Employee.find_by_id(id_)

    if employee:
        try:
            name = input("Enter the employee's new name: ")
            employee.name = name
            job_title = input("Enter the employee's new job title: ")
            employee.job_title = job_title
            department_id = input("Enter the employee's new department ID: ")
            employee.department_id = department_id

            employee.update()
            print(f"Update successful: {employee}")  # Fixed string formatting
        except Exception as exc:
            print("Error updating employee: ", exc)
    else:
        print(f"Employee {id_} not found")

def delete_employee():
    id_ = input("Enter the employee's ID: ")
    employee = Employee.find_by_id(id_)
    if employee:
        employee.delete()
        print(f"Employee {id_} deleted")
    else:
        print(f"Employee {id_} not found")

def list_department_employees():
    department_id = input("Enter the department ID: ")
    department = Department.find_by_id(department_id)
    if department:
        employees = department.employees()
        if employees:
            for employee in employees:
                print(employee)
        else:
            print(f"No employees found in Department {department_id}")
    else:
        print(f'Department {department_id} not found')